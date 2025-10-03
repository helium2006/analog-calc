'''展示FET输出特性曲线、转移特性曲线、静态工作点及图解法结果
'''

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from fet_calc.gui.gui_methord.draw_diagram.generate_figure import GenerateFigure

class ShowDiagram:
    """展示FET特性曲线和图解法结果的类"""
    
    def __init__(self, parent_output=None, parent_transfer=None, params=None):
        """初始化ShowDiagram类
        
        Args:
            parent_output: 输出特性曲线画布的父容器
            parent_transfer: 转移特性曲线画布的父容器
            params: 参数字典，包含FET类型和各种参数
        """
        self.parent_output = parent_output
        self.parent_transfer = parent_transfer
        self.params = params if params is not None else {}
        self.generate_figure = GenerateFigure()
        self.canvas_output = None  # 用于存储输出特性曲线画布
        self.canvas_transfer = None  # 用于存储转移特性曲线画布
        self.canvas_graphical = None  # 用于存储图解法画布
        
    def show_characteristic_curve(self, params=None):
        """显示FET的输出特性曲线和转移特性曲线，分别在两个画布上显示
        
        Args:
            params: 参数字典，如果提供则更新内部参数
        """
        # 更新参数
        if params is not None:
            self.params = params
        
        # 清除之前的画布
        self._clear_canvas()
        
        # 生成输出特性曲线图形
        fig_output = plt.figure(figsize=(6, 6))
        ax_output = fig_output.add_subplot(111)
        
        # 生成转移特性曲线图形
        fig_transfer = plt.figure(figsize=(6, 6))
        ax_transfer = fig_transfer.add_subplot(111)
        
        # 绘制JFET或MOSFET的特性曲线
        fet_type = self.params.get('fet_type', '')
        if fet_type == 'N_channel_jfet' or fet_type == 'P_channel_jfet':
            self.generate_figure._plot_jfet_characteristics(ax_output, ax_transfer, self.params)
        elif 'mosfet' in fet_type:
            self.generate_figure._plot_mosfet_characteristics(ax_output, ax_transfer, self.params)
        else:
            # 默认绘制N沟道JFET特性曲线
            default_params = self.params.copy()
            default_params['fet_type'] = 'N_channel_jfet'
            default_params['I_DSS'] = 1.0
            default_params['U_GSoff'] = -4.0
            default_params['λ'] = 0.0
            self.generate_figure._plot_jfet_characteristics(ax_output, ax_transfer, default_params)
            ax_output.text(0.5, 0.5, '未选择FET类型，默认显示N沟道JFET特性曲线', 
                         horizontalalignment='center', verticalalignment='center', transform=ax_output.transAxes)
        
        # 调整布局
        plt.tight_layout()
        
        # 在输出特性曲线画布上显示输出特性曲线
        if self.parent_output:
            self.canvas_output = FigureCanvasTkAgg(fig_output, master=self.parent_output)
            self.canvas_output.draw()
            self.canvas_output.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # 在转移特性曲线画布上显示转移特性曲线
        if self.parent_transfer:
            self.canvas_transfer = FigureCanvasTkAgg(fig_transfer, master=self.parent_transfer)
            self.canvas_transfer.draw()
            self.canvas_transfer.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def show_graphical_method(self, params=None):
        """显示图解法求解静态工作点的结果，包含转移特性曲线和图解法结果
        
        Args:
            params: 参数字典，如果提供则更新内部参数
        """
        # 更新参数
        if params is not None:
            self.params = params
        
        # 清除之前的画布
        self._clear_canvas()
        
        # 生成转移特性曲线图形
        fig_transfer = plt.figure(figsize=(6, 6))
        ax_transfer = fig_transfer.add_subplot(111)
        
        # 生成图解法图形
        fig_graphical = plt.figure(figsize=(6, 6))
        ax_graphical = fig_graphical.add_subplot(111)
        
        # 绘制转移特性曲线
        fet_type = self.params.get('fet_type', '')
        if fet_type == 'N_channel_jfet' or fet_type == 'P_channel_jfet':
            self.generate_figure._plot_jfet_characteristics(None, ax_transfer, self.params)
            self.generate_figure._plot_jfet_graphical_method(ax_graphical, self.params)
        elif 'mosfet' in fet_type:
            self.generate_figure._plot_mosfet_characteristics(None, ax_transfer, self.params)
            self.generate_figure._plot_mosfet_graphical_method(ax_graphical, self.params)
        else:
            # 默认绘制N沟道JFET
            default_params = self.params.copy()
            default_params['fet_type'] = 'N_channel_jfet'
            default_params['I_DSS'] = 1.0
            default_params['U_GSoff'] = -4.0
            default_params['λ'] = 0.0
            self.generate_figure._plot_jfet_characteristics(None, ax_transfer, default_params)
            self.generate_figure._plot_jfet_graphical_method(ax_graphical, default_params)
        
        # 调整布局
        plt.tight_layout()
        
        # 在转移特性曲线画布上显示转移特性曲线
        if self.parent_transfer:
            self.canvas_transfer = FigureCanvasTkAgg(fig_transfer, master=self.parent_transfer)
            self.canvas_transfer.draw()
            self.canvas_transfer.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # 在图解法画布上显示图解法结果
        if self.parent_output:
            self.canvas_graphical = FigureCanvasTkAgg(fig_graphical, master=self.parent_output)
            self.canvas_graphical.draw()
            self.canvas_graphical.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    def _clear_canvas(self):
        """清除之前显示的所有画布"""
        # 检查是否存在之前的框架和画布
        if hasattr(self, 'diagram_frame') and self.diagram_frame.winfo_exists():
            # 销毁框架会自动销毁其中的所有子组件
            self.diagram_frame.destroy()
        
        # 如果存在输出特性曲线画布实例，清除它
        if hasattr(self, 'canvas_output') and self.canvas_output:
            self.canvas_output.get_tk_widget().destroy()
            self.canvas_output = None
        
        # 如果存在转移特性曲线画布实例，清除它
        if hasattr(self, 'canvas_transfer') and self.canvas_transfer:
            self.canvas_transfer.get_tk_widget().destroy()
            self.canvas_transfer = None
        
        # 如果存在图解法画布实例，清除它
        if hasattr(self, 'canvas_graphical') and self.canvas_graphical:
            self.canvas_graphical.get_tk_widget().destroy()
            self.canvas_graphical = None
        
        # 清除matplotlib的当前图形
        plt.close('all')
        
    def update_params(self, params):
        """更新参数字典
        
        Args:
            params: 新的参数字典
        """
        self.params = params
        
    def clear(self):
        """清除所有显示的图形"""
        self._clear_canvas()
        
    def create_diagram_window(self, title="FET特性曲线", width=800, height=600):
        """创建一个独立的窗口来显示图形
        
        Args:
            title: 窗口标题
            width: 窗口宽度
            height: 窗口高度
            
        Returns:
            tk.Toplevel: 创建的窗口对象
        """
        # 创建新窗口
        diagram_window = tk.Toplevel(self.parent)
        diagram_window.title(title)
        diagram_window.geometry(f"{width}x{height}")
        diagram_window.resizable(True, True)
        
        # 创建一个新的ShowDiagram实例来管理这个窗口中的图形
        window_diagram = ShowDiagram(diagram_window, self.params)
        
        # 在新窗口中显示当前的图形类型
        # 默认显示特性曲线
        window_diagram.show_characteristic_curve()
        
        # 添加控制按钮
        control_frame = ttk.Frame(diagram_window)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        btn_characteristic = ttk.Button(control_frame, text="显示特性曲线", 
                                       command=window_diagram.show_characteristic_curve)
        btn_characteristic.pack(side=tk.LEFT, padx=5)
        
        btn_graphical = ttk.Button(control_frame, text="显示图解法", 
                                  command=window_diagram.show_graphical_method)
        btn_graphical.pack(side=tk.LEFT, padx=5)
        
        btn_close = ttk.Button(control_frame, text="关闭", 
                              command=diagram_window.destroy)
        btn_close.pack(side=tk.RIGHT, padx=5)
        
        return diagram_window

class DiagramTab(ttk.Frame):
    """可以嵌入到Notebook中的图形选项卡组件"""
    
    def __init__(self, parent, params=None):
        """初始化DiagramTab类
        
        Args:
            parent: 父组件（通常是ttk.Notebook）
            params: 参数字典
        """
        super().__init__(parent)
        self.parent = parent
        self.params = params if params is not None else {}
        self.show_diagram = ShowDiagram(self, self.params)
        
        # 创建控制按钮
        self._create_controls()
        
    def _create_controls(self):
        """创建控制按钮"""
        control_frame = ttk.Frame(self)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        btn_characteristic = ttk.Button(control_frame, text="显示特性曲线", 
                                       command=self.show_characteristic_curve)
        btn_characteristic.pack(side=tk.LEFT, padx=5)
        
        btn_graphical = ttk.Button(control_frame, text="显示图解法", 
                                  command=self.show_graphical_method)
        btn_graphical.pack(side=tk.LEFT, padx=5)
        
        btn_clear = ttk.Button(control_frame, text="清空图形", 
                              command=self.clear)
        btn_clear.pack(side=tk.LEFT, padx=5)
        
        btn_new_window = ttk.Button(control_frame, text="在新窗口显示", 
                                   command=self.show_in_new_window)
        btn_new_window.pack(side=tk.RIGHT, padx=5)
        
    def show_characteristic_curve(self):
        """显示特性曲线"""
        self.show_diagram.show_characteristic_curve(self.params)
        
    def show_graphical_method(self):
        """显示图解法"""
        self.show_diagram.show_graphical_method(self.params)
        
    def clear(self):
        """清空图形"""
        self.show_diagram.clear()
        
    def show_in_new_window(self):
        """在新窗口中显示图形"""
        self.show_diagram.create_diagram_window()
        
    def update_params(self, params):
        """更新参数"""
        self.params = params
        self.show_diagram.update_params(params)

# 如果作为主程序运行，则显示一个简单的演示
if __name__ == "__main__":
    root = tk.Tk()
    root.title("FET特性曲线演示")
    root.geometry("900x700")
    
    # 创建一个示例参数字典
    sample_params = {
        'fet_type': 'N_channel_jfet',
        'I_DSS': 2.0,  # 2mA
        'U_GSoff': -4.0,  # -4V
        'U_GSth': 2.0,  # 2V（用于MOSFET）
        'λ': 0.02,  # 沟道调制参数
        'R_S': 1.5,  # 1.5kΩ
        'R_G': 1.0,  # 1MΩ
        'R_L': 10.0  # 10kΩ
    }
    
    # 创建DiagramTab实例
    diagram_tab = DiagramTab(root, sample_params)
    diagram_tab.pack(fill=tk.BOTH, expand=True)
    
    # 显示特性曲线作为默认图形
    diagram_tab.show_characteristic_curve()
    
    root.mainloop()
