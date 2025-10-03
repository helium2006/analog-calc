'''使用matplotlib绘制figure
读取传入params中的参数，根据参数绘制figure，这里仅生成figure，在/gui_methord/show_figure.py中加载到tkinter的画布中
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

class GenerateFigure:
    """生成各种FET特性曲线的类"""
    
    def __init__(self):
        # 设置matplotlib中文字体
        plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
        plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
        
    def generate_characteristic_curve(self, params):
        """生成FET的输出特性曲线和转移特性曲线
        
        Args:
            params: 参数字典，包含FET类型和各种参数
            
        Returns:
            matplotlib.figure.Figure: 包含特性曲线的figure对象
        """
        fig = plt.figure(figsize=(10, 8))
        
        # 读取参数
        fet_type = params.get('fet_type', '')
        idss = params.get('I_DSS', 1.0)  # 默认1mA
        vgsoff = params.get('U_GSoff', -4.0)  # 默认-4V
        vgsth = params.get('U_GSth', 2.0)  # 默认2V
        lam = params.get('λ', 0.0)  # 沟道调制参数
        
        # 创建子图：输出特性曲线和转移特性曲线
        ax1 = fig.add_subplot(211)
        ax2 = fig.add_subplot(212)
        
        # 根据FET类型绘制不同的特性曲线
        if fet_type == 'N_channel_jfet' or fet_type == 'P_channel_jfet':
            self._plot_jfet_characteristics(ax1, ax2, params)
        elif 'mosfet' in fet_type:
            self._plot_mosfet_characteristics(ax1, ax2, params)
        else:
            # 默认绘制N沟道JFET特性曲线
            # 创建默认参数
            default_params = params.copy()
            default_params['fet_type'] = 'N_channel_jfet'
            default_params['I_DSS'] = 1.0
            default_params['U_GSoff'] = -4.0
            default_params['λ'] = 0.0
            self._plot_jfet_characteristics(ax1, ax2, default_params)
            ax1.text(0.5, 0.5, '未选择FET类型，默认显示N沟道JFET特性曲线', 
                     horizontalalignment='center', verticalalignment='center', transform=ax1.transAxes)
        
        plt.tight_layout()
        return fig
        
    def generate_graphical_method(self, params):
        """生成图解法求解静态工作点的图形
        
        Args:
            params: 参数字典，包含FET类型、电路参数等
            
        Returns:
            matplotlib.figure.Figure: 包含图解法的figure对象
        """
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        
        # 读取参数
        fet_type = params.get('fet_type', '')
        idss = params.get('I_DSS', 1.0)  # 默认1mA
        vgsoff = params.get('U_GSoff', -4.0)  # 默认-4V
        rs = params.get('RS', 1.0)  # 源极电阻，单位kΩ
        vdd = 12.0  # 假设电源电压为12V（可以从params中读取）
        
        # 绘制负载线和转移特性曲线
        if fet_type == 'N_channel_jfet' or fet_type == 'P_channel_jfet':
            self._plot_jfet_graphical_method(ax, params)
        elif 'mosfet' in fet_type:
            # 对于MOSFET，使用类似的方法但公式略有不同
            self._plot_mosfet_graphical_method(ax, params)
        else:
            # 默认绘制N沟道JFET图解法
            # 创建默认参数
            default_params = params.copy()
            default_params['fet_type'] = 'N_channel_jfet'
            default_params['I_DSS'] = 1.0
            default_params['U_GSoff'] = -4.0
            default_params['RS'] = 1.0
            default_params['U_DD'] = 12.0
            self._plot_jfet_graphical_method(ax, default_params)
            ax.text(0.5, 0.5, '未选择FET类型，默认显示N沟道JFET图解法', 
                     horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
        
        plt.tight_layout()
        return fig
        
    def _plot_jfet_characteristics(self, ax1, ax2, params):
        """绘制JFET的输出特性曲线和转移特性曲线"""
        # 从params字典获取参数
        fet_type = params.get('fet_type', '')
        idss = params.get('I_DSS', 0.0)
        vgsoff = params.get('U_GSoff', 0.0)
        lam = params.get('λ', 0.0)
        
        # 输出特性曲线（U_DS vs I_D，不同U_GS值）
        uds_values = np.linspace(0, 12, 100)  # U_DS从0到12V
        ugs_values = np.linspace(0, vgsoff, 6)  # U_GS从0到U_GSoff，取6个点
        
        # 只有当ax1不为None时才绘制输出特性曲线
        if ax1 is not None:
            for vgs in ugs_values:
                # JFET输出特性曲线公式
                if fet_type == 'N_channel_jfet':
                    # 对于N沟道JFET，U_GS <= 0
                    if vgs > 0:
                        vgs = 0
                    # 夹断电压
                    udsat = vgs - vgsoff if vgs > vgsoff else 0
                    # 线性区
                    id_linear = idss * (2 * (vgs - vgsoff) * uds_values / vgsoff**2 - uds_values**2 / vgsoff**2)
                    # 饱和区
                    id_saturation = idss * (1 - vgs / vgsoff)**2 * (1 + lam * uds_values)
                    # 合并线性区和饱和区
                    id = np.where(uds_values < udsat, id_linear, id_saturation)
                else:
                    # 对于P沟道JFET，U_GS >= 0
                    if vgs < 0:
                        vgs = 0
                    # 夹断电压
                    udsat = vgs - vgsoff if vgs < vgsoff else 0
                    # 线性区
                    id_linear = idss * (2 * (vgs - vgsoff) * uds_values / vgsoff**2 - uds_values**2 / vgsoff**2)
                    # 饱和区
                    id_saturation = idss * (1 - vgs / vgsoff)**2 * (1 + lam * uds_values)
                    # 合并线性区和饱和区
                    id = np.where(uds_values > udsat, id_linear, id_saturation)
                
                # 确保电流非负
                id = np.maximum(id, 0)
                
                ax1.plot(uds_values, id, label=f'U_GS = {vgs:.1f}V')
            
            # 设置输出特性曲线图的标题和标签
            ax1.set_title(f'{fet_type} 输出特性曲线')
            ax1.set_xlabel('漏源电压 U_DS (V)')
            ax1.set_ylabel('漏极电流 I_D (mA)')
            ax1.grid(True)
            ax1.legend()
        
        # 转移特性曲线（U_GS vs I_D，U_DS为常数）
        ugs_transfer = np.linspace(vgsoff, 0 if fet_type == 'N_channel_jfet' else 5, 100)
        # 对于N沟道JFET，U_GS从U_GSoff到0；对于P沟道JFET，U_GS从U_GSoff到5
        
        if fet_type == 'N_channel_jfet':
            id_transfer = idss * (1 - ugs_transfer / vgsoff)**2
            id_transfer = np.maximum(id_transfer, 0)  # 确保电流非负
        else:
            id_transfer = idss * (1 - ugs_transfer / vgsoff)**2
            id_transfer = np.maximum(id_transfer, 0)  # 确保电流非负

        # 只有当ax2不为None时才绘制转移特性曲线
        if ax2 is not None:
            ax2.plot(ugs_transfer, id_transfer)
            
            # 设置转移特性曲线图的标题和标签
            ax2.set_title(f'{fet_type} 转移特性曲线 (U_DS = 10V)')
            ax2.set_xlabel('栅源电压 U_GS (V)')
            ax2.set_ylabel('漏极电流 I_D (mA)')
            ax2.grid(True)
        
    def _plot_mosfet_characteristics(self, ax1, ax2, params):
        """绘制MOSFET的输出特性曲线和转移特性曲线"""
        # 从params字典获取参数
        fet_type = params.get('fet_type', '')
        idss = params.get('I_DSS', 0.0)
        vgsoff = params.get('U_GSoff', 0.0)
        vgsth = params.get('U_GSth', 0.0)
        lam = params.get('λ', 0.0)
        
        # 输出特性曲线（U_DS vs I_D，不同U_GS值）
        uds_values = np.linspace(0, 12, 100)  # U_DS从0到12V
        
        if 'enhanced' in fet_type:
            # 增强型MOSFET
            if 'N_channel' in fet_type:
                ugs_values = np.linspace(vgsth, vgsth + 4, 5)  # U_GS从U_GSth到U_GSth+4V，取5个点
                if ax1 is not None:
                    for ugs in ugs_values:
                        # 增强型N沟道MOSFET输出特性曲线公式
                        udsat = ugs - vgsth
                        # 线性区
                        id_linear = idss * 2 * (ugs - vgsth) * uds_values / (12**2) - uds_values**2 / (12**2)
                        # 饱和区
                        id_saturation = idss * (ugs - vgsth)**2 / (12**2) * (1 + lam * uds_values)
                        # 合并线性区和饱和区
                        id = np.where(uds_values < udsat, id_linear, id_saturation)
                        id = np.maximum(id, 0)  # 确保电流非负
                        ax1.plot(uds_values, id, label=f'U_GS = {ugs:.1f}V')
                
                # 转移特性曲线
                ugs_transfer = np.linspace(vgsth, vgsth + 5, 100)
                id_transfer = idss * (ugs_transfer - vgsth)**2 / (12**2)
                id_transfer = np.maximum(id_transfer, 0)
                if ax2 is not None:
                    ax2.plot(ugs_transfer, id_transfer)
            else:
                # 增强型P沟道MOSFET
                ugs_values = np.linspace(-vgsth - 4, -vgsth, 5)  # U_GS从-U_GSth-4到-U_GSthV，取5个点
                if ax1 is not None:
                    for ugs in ugs_values:
                        # 增强型P沟道MOSFET输出特性曲线公式
                        udsat = ugs + vgsth
                        # 线性区
                        id_linear = idss * 2 * (ugs + vgsth) * uds_values / (12**2) - uds_values**2 / (12**2)
                        # 饱和区
                        id_saturation = idss * (ugs + vgsth)**2 / (12**2) * (1 + lam * uds_values)
                        # 合并线性区和饱和区
                        id = np.where(uds_values > udsat, id_linear, id_saturation)
                        id = np.maximum(id, 0)  # 确保电流非负
                        ax1.plot(uds_values, id, label=f'U_GS = {ugs:.1f}V')
                
                # 转移特性曲线
                ugs_transfer = np.linspace(-vgsth - 5, -vgsth, 100)
                id_transfer = idss * (ugs_transfer + vgsth)**2 / (12**2)
                id_transfer = np.maximum(id_transfer, 0)
                if ax2 is not None:
                    ax2.plot(ugs_transfer, id_transfer)
        else:
            # 耗尽型MOSFET
            if 'N_channel' in fet_type:
                ugs_values = np.linspace(vgsoff, 2, 5)  # U_GS从U_GSoff到2V，取5个点
                if ax1 is not None:
                    for ugs in ugs_values:
                        # 耗尽型N沟道MOSFET输出特性曲线公式
                        udsat = ugs - vgsoff if ugs > vgsoff else 0
                        # 线性区
                        id_linear = idss * (2 * (ugs - vgsoff) * uds_values / vgsoff**2 - uds_values**2 / vgsoff**2)
                        # 饱和区
                        id_saturation = idss * (1 - ugs / vgsoff)**2 * (1 + lam * uds_values)
                        # 合并线性区和饱和区
                        id = np.where(uds_values < udsat, id_linear, id_saturation)
                        id = np.maximum(id, 0)  # 确保电流非负
                        ax1.plot(uds_values, id, label=f'U_GS = {ugs:.1f}V')
                
                # 转移特性曲线
                ugs_transfer = np.linspace(vgsoff, 2, 100)
                id_transfer = idss * (1 - ugs_transfer / vgsoff)**2
                id_transfer = np.maximum(id_transfer, 0)
                if ax2 is not None:
                    ax2.plot(ugs_transfer, id_transfer)
            else:
                # 耗尽型P沟道MOSFET
                ugs_values = np.linspace(0, -vgsoff, 5)  # U_GS从0到-U_GSoff，取5个点
                if ax1 is not None:
                    for ugs in ugs_values:
                        # 耗尽型P沟道MOSFET输出特性曲线公式
                        udsat = ugs + vgsoff if ugs < -vgsoff else 0
                        # 线性区
                        id_linear = idss * (2 * (ugs + vgsoff) * uds_values / vgsoff**2 - uds_values**2 / vgsoff**2)
                        # 饱和区
                        id_saturation = idss * (1 + ugs / vgsoff)**2 * (1 + lam * uds_values)
                        # 合并线性区和饱和区
                        id = np.where(uds_values > udsat, id_linear, id_saturation)
                        id = np.maximum(id, 0)  # 确保电流非负
                        ax1.plot(uds_values, id, label=f'U_GS = {ugs:.1f}V')
                
                # 转移特性曲线
                ugs_transfer = np.linspace(0, -vgsoff, 100)
                id_transfer = idss * (1 + ugs_transfer / vgsoff)**2
                id_transfer = np.maximum(id_transfer, 0)
                if ax2 is not None:
                    ax2.plot(ugs_transfer, id_transfer)
        
        # 设置输出特性曲线图的标题和标签
        if ax1 is not None:
            ax1.set_title(f'{fet_type} 输出特性曲线')
            ax1.set_xlabel('漏源电压 U_DS (V)')
            ax1.set_ylabel('漏极电流 I_D (mA)')
            ax1.grid(True)
            ax1.legend()
        
        # 设置转移特性曲线图的标题和标签
        if ax2 is not None:
            ax2.set_title(f'{fet_type} 转移特性曲线 (U_DS = 10V)')
            ax2.set_xlabel('栅源电压 U_GS (V)')
            ax2.set_ylabel('漏极电流 I_D (mA)')
            ax2.grid(True)
        
    def _plot_jfet_graphical_method(self, ax, params):
        """绘制JFET图解法求解静态工作点的图形"""
        # 从params字典获取参数
        fet_type = params.get('fet_type', '')
        idss = params.get('I_DSS', 0.0)
        vgsoff = params.get('U_GSoff', 0.0)
        rs = params.get('RS', 0.0)
        vdd = params.get('U_DD', 0.0)
        
        # 只有当ax不为None时才执行绘图操作
        if ax is not None:
            # 绘制转移特性曲线
            if fet_type == 'N_channel_jfet':
                vgs = np.linspace(vgsoff, 0, 100)
            else:
                vgs = np.linspace(0, -vgsoff, 100)  # 对于P沟道JFET
                
            id_transfer = idss * (1 - vgs / vgsoff)**2 if fet_type == 'N_channel_jfet' else idss * (1 + vgs / vgsoff)**2
            id_transfer = np.maximum(id_transfer, 0)  # 确保电流非负
            
            ax.plot(vgs, id_transfer, 'b-', linewidth=2, label='转移特性曲线')
            
            # 绘制负载线（对于自给偏置电路）
            # 负载线方程：U_GS = -I_D * R_S
            vgs_load = np.linspace(min(vgs), max(vgs), 100)
            if fet_type == 'N_channel_jfet':
                id_load = -vgs_load / rs
            else:
                id_load = vgs_load / rs  # 对于P沟道JFET，符号相反
            
            # 限制负载线的电流为非负值
            valid_indices = id_load >= 0
            vgs_load = vgs_load[valid_indices]
            id_load = id_load[valid_indices]
            
            ax.plot(vgs_load, id_load, 'r--', linewidth=2, label=f'负载线 (RS = {rs}kΩ)')
            
            # 计算静态工作点（转移特性曲线和负载线的交点）
            # 使用数值方法求解交点
            from scipy.optimize import fsolve
            
            def equations(variables):
                vgsq = variables[0]
                if fet_type == 'N_channel_jfet':
                    idq_transfer = idss * (1 - vgsq / vgsoff)**2
                    idq_load = -vgsq / rs
                else:
                    idq_transfer = idss * (1 + vgsq / vgsoff)**2
                    idq_load = vgsq / rs
                return idq_transfer - idq_load
            
            # 寻找合适的初始猜测值
            if fet_type == 'N_channel_jfet':
                initial_guess = vgsoff / 2  # 初始猜测为U_GSoff的一半
            else:
                initial_guess = -vgsoff / 2  # 对于P沟道JFET
                
            try:
                solution = fsolve(equations, initial_guess)
                vgsq = solution[0]
                if fet_type == 'N_channel_jfet':
                    idq = idss * (1 - vgsq / vgsoff)**2
                else:
                    idq = idss * (1 + vgsq / vgsoff)**2
                    
                # 绘制静态工作点
                ax.plot(vgsq, idq, 'go', markersize=8, label=f'静态工作点: U_GSQ={vgsq:.2f}V, I_DQ={idq:.2f}mA')
            except:
                # 如果求解失败，仍然可以显示图形但不标记静态工作点
                pass
            
            # 设置图形标题和标签
            ax.set_title(f'{fet_type} 自给偏置电路图解法')
            ax.set_xlabel('栅源电压 U_GS (V)')
            ax.set_ylabel('漏极电流 I_D (mA)')
            ax.grid(True)
            ax.legend()
        
    def _plot_mosfet_graphical_method(self, ax, params):
        """绘制MOSFET图解法求解静态工作点的图形"""
        # 从params字典获取参数
        fet_type = params.get('fet_type', '')
        idss = params.get('I_DSS', 0.0)
        vgsoff = params.get('U_GSoff', 0.0)
        vgsth = params.get('U_GSth', 0.0)
        rs = params.get('RS', 0.0)
        vdd = params.get('U_DD', 0.0)
        
        # 只有当ax不为None时才执行绘图操作
        if ax is not None:
            # 绘制转移特性曲线
            if 'enhanced' in fet_type:
                if 'N_channel' in fet_type:
                    vgs = np.linspace(vgsth, vgsth + 5, 100)
                    id_transfer = idss * (vgs - vgsth)**2 / (12**2)  # 简化模型
                else:
                    vgs = np.linspace(-vgsth - 5, -vgsth, 100)
                    id_transfer = idss * (vgs + vgsth)**2 / (12**2)  # 简化模型
            else:
                # 耗尽型MOSFET
                if 'N_channel' in fet_type:
                    vgs = np.linspace(vgsoff, 2, 100)
                    id_transfer = idss * (1 - vgs / vgsoff)**2
                else:
                    vgs = np.linspace(0, -vgsoff, 100)
                    id_transfer = idss * (1 + vgs / vgsoff)**2
                    
            id_transfer = np.maximum(id_transfer, 0)  # 确保电流非负
            
            ax.plot(vgs, id_transfer, 'b-', linewidth=2, label='转移特性曲线')
            
            # 绘制负载线（对于自给偏置电路）
            # 负载线方程：U_GS = -I_D * R_S
            vgs_load = np.linspace(min(vgs), max(vgs), 100)
            if 'N_channel' in fet_type:
                id_load = -vgs_load / rs
            else:
                id_load = vgs_load / rs  # 对于P沟道，符号相反
            
            # 限制负载线的电流为非负值
            valid_indices = id_load >= 0
            vgs_load = vgs_load[valid_indices]
            id_load = id_load[valid_indices]
            
            ax.plot(vgs_load, id_load, 'r--', linewidth=2, label=f'负载线 (RS = {rs}kΩ)')
            
            # 计算静态工作点（转移特性曲线和负载线的交点）
            # 使用数值方法求解交点
            from scipy.optimize import fsolve
            
            def equations(variables):
                vgsq = variables[0]
                if 'enhanced' in fet_type:
                    if 'N_channel' in fet_type:
                        idq_transfer = idss * (vgsq - vgsth)**2 / (12**2)
                        idq_load = -vgsq / rs
                    else:
                        idq_transfer = idss * (vgsq + vgsth)**2 / (12**2)
                        idq_load = vgsq / rs
                else:
                    if 'N_channel' in fet_type:
                        idq_transfer = idss * (1 - vgsq / vgsoff)**2
                        idq_load = -vgsq / rs
                    else:
                        idq_transfer = idss * (1 + vgsq / vgsoff)**2
                        idq_load = vgsq / rs
                return idq_transfer - idq_load
            
            # 寻找合适的初始猜测值
            if 'enhanced' in fet_type:
                if 'N_channel' in fet_type:
                    initial_guess = vgsth + 1  # 增强型N沟道，初始猜测为开启电压+1V
                else:
                    initial_guess = -vgsth - 1  # 增强型P沟道，初始猜测为-开启电压-1V
            else:
                if 'N_channel' in fet_type:
                    initial_guess = vgsoff / 2  # 耗尽型N沟道，初始猜测为U_GSoff的一半
                else:
                    initial_guess = -vgsoff / 2  # 耗尽型P沟道
                    
            try:
                solution = fsolve(equations, initial_guess)
                vgsq = solution[0]
                
                if 'enhanced' in fet_type:
                    if 'N_channel' in fet_type:
                        idq = idss * (vgsq - vgsth)**2 / (12**2)
                    else:
                        idq = idss * (vgsq + vgsth)**2 / (12**2)
                else:
                    if 'N_channel' in fet_type:
                        idq = idss * (1 - vgsq / vgsoff)**2
                    else:
                        idq = idss * (1 + vgsq / vgsoff)**2
                        
                # 绘制静态工作点
                ax.plot(vgsq, idq, 'go', markersize=8, label=f'静态工作点: U_GSQ={vgsq:.2f}V, I_DQ={idq:.2f}mA')
            except:
                # 如果求解失败，仍然可以显示图形但不标记静态工作点
                pass
            
            # 设置图形标题和标签
            ax.set_title(f'{fet_type} 自给偏置电路图解法')
            ax.set_xlabel('栅源电压 U_GS (V)')
            ax.set_ylabel('漏极电流 I_D (mA)')
            ax.grid(True)
            ax.legend()
