'''fet_calc的主窗口，属于analog_calc下的一个部分
这里是tkinter的主窗口部分，包含所有的组件,
全部的操作均基于字典params，所有的操作都是读取字典里面的参数，
并将结果写入字典params
最终返回的结果也要从字典params中读取
'''

from tkinter import *
from tkinter.ttk import *
from fet_calc.gui.component.frame_components import FrameComponents
from fet_calc.gui.component.label_components import LabelComponents
from fet_calc.gui.component.radio_button_components import RadioButtonComponents
from fet_calc.gui.component.input_components import InputComponents
from fet_calc.gui.component.button_components import ButtonComponents
from fet_calc.gui.component.canvas_components import CanvasComponents
from fet_calc.gui.choose_fet_type_check_box import ChooseFetTypeCheckBox
from fet_calc.gui.show_diagram import ShowDiagram
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# 导入计算函数
from fet_calc.utils.fet_using_situations.DC_use.basic_use import basic_use
from fet_calc.utils.fet_using_situations.DC_use.DC_div_voltage_bia import calc_I_D_DC_div_voltage_bia
from fet_calc.utils.fet_using_situations.DC_use.DC_self_bia import calc_I_D_DC_self_bia
from fet_calc.utils.fet_using_situations.amplifer_use.shared_D import calc_shared_D_An
# 导入电阻单位转换函数
from fet_calc.utils.data_process.unit_conversion.resistor_conversion import MΩ_to_kΩ
from fet_calc.utils.fet_using_situations.amplifer_use.shared_G import calc_shared_G_An
from fet_calc.utils.fet_using_situations.amplifer_use.shared_S import calc_shared_S_An

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        
        # 创建框架组件
        self.tk_frame_mg91hvtk = FrameComponents.create_fet_type_frame(self)  # FET类型选择框架
        self.tk_frame_mg924gdb = FrameComponents.create_dc_mode_frame(self)  # 直流模式选择框架
        self.tk_frame_mg92f171 = FrameComponents.create_amplifier_frame(self)  # 放大电路结构选择框架
        self.tk_frame_mg93erze = FrameComponents.create_params_frame(self)  # 参数输入框架
        
        # 创建标签组件
        self.tk_label_mg91ic94 = LabelComponents.create_fet_type_label(self.tk_frame_mg91hvtk)  # FET类型选择标签
        self.tk_label_mg9265l6 = LabelComponents.create_dc_mode_label(self.tk_frame_mg924gdb)  # 直流模式选择标签
        self.tk_label_mg92fk07 = LabelComponents.create_amplifier_label(self.tk_frame_mg92f171)  # 放大电路结构选择标签
        self.tk_label_mg93fn4c = LabelComponents.create_params_label(self.tk_frame_mg93erze)  # 参数输入标签
        self.tk_label_mg96mdps = LabelComponents.create_idss_label(self.tk_frame_mg93erze)  # I_DSS标签
        self.tk_label_mg96stkb = LabelComponents.create_phi_g_label(self.tk_frame_mg93erze)  # ϕ_G标签
        self.tk_label_mg96vitf = LabelComponents.create_phi_s_label(self.tk_frame_mg93erze)  # ϕ_S标签
        self.tk_label_mg96ycfj = LabelComponents.create_phi_d_label(self.tk_frame_mg93erze)  # ϕ_D标签
        self.tk_label_mg9797uz = LabelComponents.create_vgsoff_label(self.tk_frame_mg93erze)  # U_GSoff标签
        self.tk_label_mg97diaf = LabelComponents.create_vgsth_label(self.tk_frame_mg93erze)  # U_GSth标签
        self.tk_label_mg97hw43 = LabelComponents.create_lambda_label(self.tk_frame_mg93erze)  # λ标签
        self.tk_label_mg97lmx6 = LabelComponents.create_rg_label(self.tk_frame_mg93erze)  # R_G标签
        self.tk_label_mg97lq20 = LabelComponents.create_rs_label(self.tk_frame_mg93erze)  # R_S标签
        self.tk_label_mg97lsis = LabelComponents.create_rd_label(self.tk_frame_mg93erze)  # R_D标签
        self.tk_label_mg97onzf = LabelComponents.create_rl_label(self.tk_frame_mg93erze)  # R_L标签
        self.tk_label_mg97rmar = LabelComponents.create_gm_label(self.tk_frame_mg93erze)  # gm标签
        self.tk_label_mgamn5wl = LabelComponents.create_resistor_unit_label(self.tk_frame_mg93erze)  # 电阻单位标签
        self.tk_label_mgaj3th1 = LabelComponents.create_kn_label(self.tk_frame_mg93erze)  # Kn标签
        
        # 创建单选按钮组件
        self.tk_radio_button_mg91iuvu = RadioButtonComponents.create_p_channel_jfet_rb(self.tk_frame_mg91hvtk)  # P沟道JFET单选按钮
        self.tk_radio_button_mg91phml = RadioButtonComponents.create_n_channel_jfet_rb(self.tk_frame_mg91hvtk)  # N沟道JFET单选按钮
        self.tk_radio_button_mg91udyh = RadioButtonComponents.create_enhanced_n_channel_mosfet_rb(self.tk_frame_mg91hvtk)  # 增强型N沟道MOSFET单选按钮
        self.tk_radio_button_mg91uh30 = RadioButtonComponents.create_enhanced_p_channel_mosfet_rb(self.tk_frame_mg91hvtk)  # 增强型P沟道MOSFET单选按钮
        self.tk_radio_button_mg91uibx = RadioButtonComponents.create_depletion_n_channel_mosfet_rb(self.tk_frame_mg91hvtk)  # 耗尽型N沟道MOSFET单选按钮
        self.tk_radio_button_mg91ujgb = RadioButtonComponents.create_depletion_p_channel_mosfet_rb(self.tk_frame_mg91hvtk)  # 耗尽型P沟道MOSFET单选按钮
        self.tk_radio_button_mg92ar2h = RadioButtonComponents.create_basic_use_rb(self.tk_frame_mg924gdb)  # 基本使用单选按钮
        self.tk_radio_button_mg92avln = RadioButtonComponents.create_dc_self_bia_rb(self.tk_frame_mg924gdb)  # 直流自给偏置单选按钮
        self.tk_radio_button_mg92bsbu = RadioButtonComponents.create_dc_div_voltage_bia_rb(self.tk_frame_mg924gdb)  # 直流分压偏置单选按钮
        self.tk_radio_button_mg92wu8e = RadioButtonComponents.create_shared_d_rb(self.tk_frame_mg92f171)  # 共漏极单选按钮
        self.tk_radio_button_mg92wvrz = RadioButtonComponents.create_shared_g_rb(self.tk_frame_mg92f171)  # 共栅极单选按钮
        self.tk_radio_button_mg92wzuu = RadioButtonComponents.create_shared_s_rb(self.tk_frame_mg92f171)  # 共源极单选按钮
        self.tk_radio_button_mg97f26p = RadioButtonComponents.create_lambda_enable_rb(self.tk_frame_mg93erze)  # 启用沟道调制参数单选按钮
        self.tk_radio_button_mgaj6t8d = RadioButtonComponents.create_resistor_unit_kilo_rb(self.tk_frame_mg93erze)  # 千欧电阻单位单选按钮
        self.tk_radio_button_mgaj70wm = RadioButtonComponents.create_resistor_unit_mega_rb(self.tk_frame_mg93erze)  # 兆欧电阻单位单选按钮
        
        # 创建输入框组件
        self.tk_input_mg96qtal = InputComponents.create_idss_input(self.tk_frame_mg93erze)  # I_DSS输入框
        self.tk_input_mg96tbh0 = InputComponents.create_phi_g_input(self.tk_frame_mg93erze)  # ϕ_G输入框
        self.tk_input_mg96w3ln = InputComponents.create_phi_s_input(self.tk_frame_mg93erze)  # ϕ_S输入框
        self.tk_input_mg96yn71 = InputComponents.create_phi_d_input(self.tk_frame_mg93erze)  # ϕ_D输入框
        self.tk_input_mg97bf2d = InputComponents.create_vgsoff_input(self.tk_frame_mg93erze)  # U_GSoff输入框
        self.tk_input_mg97dzwg = InputComponents.create_vgsth_input(self.tk_frame_mg93erze)  # U_GSth输入框
        self.tk_input_mg97iv4q = InputComponents.create_lambda_input(self.tk_frame_mg93erze)  # λ输入框
        self.tk_input_mg97lopj = InputComponents.create_rg_input(self.tk_frame_mg93erze)  # R_G输入框
        self.tk_input_mg97lrc9 = InputComponents.create_rs_input(self.tk_frame_mg93erze)  # R_S输入框
        self.tk_input_mg97ltzk = InputComponents.create_rd_input(self.tk_frame_mg93erze)  # R_D输入框
        self.tk_input_mg97ope1 = InputComponents.create_rl_input(self.tk_frame_mg93erze)  # R_L输入框
        self.tk_input_mg97shp5 = InputComponents.create_gm_input(self.tk_frame_mg93erze)  # gm输入框
        self.tk_input_mgaj4ik9 = InputComponents.create_kn_input(self.tk_frame_mg93erze)  # Kn输入框
        
        # 创建按钮组件
        self.tk_button_mg9342jb = ButtonComponents.create_calculate_id_button(self.tk_frame_mg924gdb)  # 计算漏极电流按钮
        self.tk_button_mg935d0a = ButtonComponents.create_calculate_amplifier_button(self.tk_frame_mg92f171)  # 计算放大系数按钮
        self.tk_button_mg981wct = ButtonComponents.create_show_characteristic_curve_button(self)  # 显示特性曲线按钮
        self.tk_button_mg9839ib = ButtonComponents.create_clear_characteristic_curve_button(self)  # 清空特性曲线按钮
        self.tk_button_mg987q8g = ButtonComponents.create_show_graphical_method_button(self)  # 显示图解法按钮
        self.tk_button_mg989afn = ButtonComponents.create_calculate_all_button(self)  # 计算全部按钮
        
        # 创建画布和文本框组件
        self.tk_canvas_mg97v16m = CanvasComponents.create_characteristic_curve_canvas(self)  # 特性曲线画布
        self.tk_canvas_mg97w0hx = CanvasComponents.create_graphical_method_canvas(self)  # 图解法画布
        self.tk_text_mg97ybm0 = CanvasComponents.create_result_text(self)  # 结果显示文本框
        
        # 初始化ShowDiagram实例，使用两个不同的画布作为父容器
        self.diagram = ShowDiagram(self.tk_canvas_mg97v16m, self.tk_canvas_mg97w0hx)
        
        # 添加参数存储字典
        self.params = {
            'I_DSS': 0.0,  # I_DSS
            'fet_type': '',  # fet类型
            'ϕ_G': 0.0,  # 栅极电位
            'ϕ_D': 0.0,  # 漏极电位
            'ϕ_S': 0.0,  # 源极电位
            'U_GSoff': 0.0,  # 截止栅源电压
            'U_GSth': 0.0,  # 开启电压
            'λ': 0.0,  # 沟道调制参数
            'Kn': 0.0,  # 跨导参数
            'RS': 0.0,  # 源极电阻
            'RD': 0.0,  # 漏极电阻
            'RG': 0.0,  # 栅极电阻
            'RL': 0.0,  # 负载电阻
            'DC_use_situation': '',  # 直流使用场景
            'amplifier_situation': '',  # 放大电路类型
            'gm': 0.0,  # 跨导
            'An': 0.0,  # 放大倍数
            'ID': 0.0,  # 漏极电流
            'workspace': '',  # 器件工作区域
            'U_GS': 0.0,  # 栅源电压
            'U_DS': 0.0,  # 漏源电压
            'U_GD': 0.0,  # 栅漏电压
            'valid_root': 0.0,  # 有效根
            'I_D_basic_use': 0.0,  # 基本使用下的漏极电流
            'I_D_DC_self_bia': 0.0,  # 直流自给偏置下的漏极电流
            'I_D_DC_div_voltage_bia': 0.0  # 直流分压偏置下的漏极电流
        }
        #print(self.params)
        # 创建FET类型选择器
        self.fet_type_selector = ChooseFetTypeCheckBox(self.tk_frame_mg91hvtk, self.params)
        
        # 初始化其他radio button的变量
        self.dc_use_situation_var = StringVar()
        self.amplifier_situation_var = StringVar()
        self.lambda_var = BooleanVar()
        self.resistor_unit_var = StringVar()
        self.resistor_unit_var.set('kΩ')  # 默认电阻单位为kΩ
        
        self.tk_radio_button_mg92ar2h.config(variable=self.dc_use_situation_var, value='basic_use')
        self.tk_radio_button_mg92avln.config(variable=self.dc_use_situation_var, value='DC_self_bia')
        self.tk_radio_button_mg92bsbu.config(variable=self.dc_use_situation_var, value='DC_div_voltage_bia')
        
        self.tk_radio_button_mg92wu8e.config(variable=self.amplifier_situation_var, value='shared_D')
        self.tk_radio_button_mg92wvrz.config(variable=self.amplifier_situation_var, value='shared_G')
        self.tk_radio_button_mg92wzuu.config(variable=self.amplifier_situation_var, value='shared_S')
        
        self.tk_radio_button_mg97f26p.config(variable=self.lambda_var)
        
        # 设置电阻单位单选按钮的变量绑定
        self.tk_radio_button_mgaj6t8d.config(variable=self.resistor_unit_var, value='kΩ')
        self.tk_radio_button_mgaj70wm.config(variable=self.resistor_unit_var, value='MΩ')
        
        # 绑定事件处理函数
        self.__bind_events()
        
    def __win(self):
        self.title("fet calc")
        # 设置窗口大小、居中
        width = 1000
        height = 700
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
        
    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
        
    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
        
    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
        
    def __bind_events(self):
        """绑定事件处理函数"""
        # 绑定计算按钮事件
        self.tk_button_mg9342jb.config(command=self.calculate_id)
        self.tk_button_mg935d0a.config(command=self.calculate_amplifier)
        self.tk_button_mg989afn.config(command=self.calculate_all)
        self.tk_button_mg981wct.config(command=self.show_characteristic_curve)
        self.tk_button_mg9839ib.config(command=self.clear_characteristic_curve)
        self.tk_button_mg987q8g.config(command=self.show_graphical_method)
        

        
        # 绑定沟道调制参数启用事件
        self.lambda_var.trace_add("write", self.on_lambda_change)
        
    def on_lambda_change(self, *args):
        """沟道调制参数启用状态改变时的处理函数"""
        pass
        
    def read_input_values(self):
        """从输入框读取参数值"""
        try:
            self.params['I_DSS'] = float(self.tk_input_mg96qtal.get()) if self.tk_input_mg96qtal.get() else 0.0
            self.params['ϕ_G'] = float(self.tk_input_mg96tbh0.get()) if self.tk_input_mg96tbh0.get() else 0.0
            self.params['ϕ_S'] = float(self.tk_input_mg96w3ln.get()) if self.tk_input_mg96w3ln.get() else 0.0
            self.params['ϕ_D'] = float(self.tk_input_mg96yn71.get()) if self.tk_input_mg96yn71.get() else 0.0
            self.params['U_GSoff'] = float(self.tk_input_mg97bf2d.get()) if self.tk_input_mg97bf2d.get() else 0.0
            self.params['U_GSth'] = float(self.tk_input_mg97dzwg.get()) if self.tk_input_mg97dzwg.get() else 0.0
            if self.lambda_var.get():
                self.params['λ'] = float(self.tk_input_mg97iv4q.get()) if self.tk_input_mg97iv4q.get() else 0.0
            self.params['RG'] = float(self.tk_input_mg97lopj.get()) if self.tk_input_mg97lopj.get() else 0.0
            self.params['RS'] = float(self.tk_input_mg97lrc9.get()) if self.tk_input_mg97lrc9.get() else 0.0
            self.params['RD'] = float(self.tk_input_mg97ltzk.get()) if self.tk_input_mg97ltzk.get() else 0.0
            self.params['RL'] = float(self.tk_input_mg97ope1.get()) if self.tk_input_mg97ope1.get() else 0.0
            self.params['gm'] = float(self.tk_input_mg97shp5.get()) if self.tk_input_mg97shp5.get() else 0.0
            self.params['Kn'] = float(self.tk_input_mgaj4ik9.get()) if self.tk_input_mgaj4ik9.get() else 0.0
            self.params['DC_use_situation'] = self.dc_use_situation_var.get()
            self.params['amplifier_situation'] = self.amplifier_situation_var.get()
            
            # 检查电阻单位，如果是兆欧姆(MΩ)，则转换为千欧姆(kΩ)
            if self.resistor_unit_var.get() == 'MΩ':
                self.params['RG'] = MΩ_to_kΩ(self.params['RG'])
                self.params['RS'] = MΩ_to_kΩ(self.params['RS'])
                self.params['RD'] = MΩ_to_kΩ(self.params['RD'])
                self.params['RL'] = MΩ_to_kΩ(self.params['RL'])
        except ValueError:
            self.tk_text_mg97ybm0.delete(1.0, END)
            self.tk_text_mg97ybm0.insert(END, "输入参数格式错误，请输入有效的数值！")
        #print(self.params)

    def calculate_id(self):
        """计算漏极电流"""
        self.read_input_values()
        
        # 根据直流使用场景调用相应的计算函数
        try:
            self.tk_text_mg97ybm0.delete(1.0, END)
            self.tk_text_mg97ybm0.insert(END, "计算直流模式下的漏极电流：\n")
            self.tk_text_mg97ybm0.insert(END, f"FET类型: {self.params['fet_type']}\n")
            self.tk_text_mg97ybm0.insert(END, f"直流模式: {self.params['DC_use_situation']}\n")
            
            # 调用相应的计算函数
            if self.params['DC_use_situation'] == 'basic_use':
                self.params = basic_use(self.params)
                self.tk_text_mg97ybm0.insert(END, f"基本使用下的漏极电流 I_D = {self.params.get('I_D_basic_use', '未计算出')} mA\n")
            elif self.params['DC_use_situation'] == 'DC_self_bia':
                self.params = calc_I_D_DC_self_bia(self.params)
                self.tk_text_mg97ybm0.insert(END, f"自给偏置下的漏极电流 I_D = {self.params.get('I_D_DC_self_bia', '未计算出')} mA\n")
            elif self.params['DC_use_situation'] == 'DC_div_voltage_bia':
                self.params = calc_I_D_DC_div_voltage_bia(self.params)
                self.tk_text_mg97ybm0.insert(END, f"分压偏置下的漏极电流 I_D = {self.params.get('I_D_DC_div_voltage_bia', '未计算出')} mA\n")
            else:
                self.tk_text_mg97ybm0.insert(END, "请选择有效的直流使用场景\n")
                
            # 显示计算得到的所有相关参数
            self.tk_text_mg97ybm0.insert(END, "\n计算结果参数：\n")
            for key, value in self.params.items():
                if key.startswith('I_D'):
                    self.tk_text_mg97ybm0.insert(END, f"{key}: {value}\n")
        except Exception as e:
            self.tk_text_mg97ybm0.delete(1.0, END)
            self.tk_text_mg97ybm0.insert(END, f"计算过程中发生错误：{str(e)}")
        print(self.params)
    def calculate_amplifier(self):
        """计算放大系数"""
        self.read_input_values()
        
        # 根据放大电路类型调用相应的计算函数
        try:
            self.tk_text_mg97ybm0.delete(1.0, END)
            self.tk_text_mg97ybm0.insert(END, "计算放大系数：\n")
            self.tk_text_mg97ybm0.insert(END, f"FET类型: {self.params['fet_type']}\n")
            self.tk_text_mg97ybm0.insert(END, f"放大电路类型: {self.params['amplifier_situation']}\n")
            
            # 调用相应的计算函数
            if self.params['amplifier_situation'] == 'shared_S':
                self.params = calc_shared_S_An(self.params)
                self.tk_text_mg97ybm0.insert(END, f"共源放大器的放大系数 A_v = {self.params.get('An', '未计算出')}\n")
            elif self.params['amplifier_situation'] == 'shared_G':
                self.params = calc_shared_G_An(self.params)
                self.tk_text_mg97ybm0.insert(END, f"共栅放大器的放大系数 A_v = {self.params.get('An', '未计算出')}\n")
            elif self.params['amplifier_situation'] == 'shared_D':
                self.params = calc_shared_D_An(self.params)
                self.tk_text_mg97ybm0.insert(END, f"共漏放大器的放大系数 A_v = {self.params.get('An', '未计算出')}\n")
            else:
                self.tk_text_mg97ybm0.insert(END, "请选择有效的放大电路类型\n")
                
            # 显示相关的跨导参数
            if 'gm' in self.params:
                self.tk_text_mg97ybm0.insert(END, f"跨导 g_m = {self.params['gm']} mS\n")
            #print(self.params)
        except Exception as e:
            self.tk_text_mg97ybm0.delete(1.0, END)
            self.tk_text_mg97ybm0.insert(END, f"计算过程中发生错误：{str(e)}")
        
    def calculate_all(self):
        """计算全部参数"""
        self.read_input_values()
        
        # 调用所有的计算函数
        try:
            self.tk_text_mg97ybm0.delete(1.0, END)
            self.tk_text_mg97ybm0.insert(END, "计算全部参数：\n")
            self.tk_text_mg97ybm0.insert(END, f"FET类型: {self.params['fet_type']}\n")
            self.tk_text_mg97ybm0.insert(END, f"直流模式: {self.params['DC_use_situation']}\n")
            self.tk_text_mg97ybm0.insert(END, f"放大电路类型: {self.params['amplifier_situation']}\n")
            
            # 调用直流相关的计算函数
            self.tk_text_mg97ybm0.insert(END, "\n直流参数计算结果：\n")
            # 基本使用
            self.params = basic_use(self.params)
            self.tk_text_mg97ybm0.insert(END, f"基本使用下的漏极电流 I_D = {self.params.get('I_D_basic_use', '未计算出')} mA\n")
            
            # 自给偏置
            self.params = calc_I_D_DC_self_bia(self.params)
            self.tk_text_mg97ybm0.insert(END, f"自给偏置下的漏极电流 I_D = {self.params.get('I_D_DC_self_bia', '未计算出')} mA\n")
            
            # 分压偏置
            self.params = calc_I_D_DC_div_voltage_bia(self.params)
            self.tk_text_mg97ybm0.insert(END, f"分压偏置下的漏极电流 I_D = {self.params.get('I_D_DC_div_voltage_bia', '未计算出')} mA\n")
            
            # 调用放大器相关的计算函数
            self.tk_text_mg97ybm0.insert(END, "\n放大器参数计算结果：\n")
            
            # 共源放大器
            temp_params = self.params.copy()
            temp_params = calc_shared_S_An(temp_params)
            self.tk_text_mg97ybm0.insert(END, f"共源放大器的放大系数 A_v = {temp_params.get('An', '未计算出')}\n")
            
            # 共栅放大器
            temp_params = self.params.copy()
            temp_params = calc_shared_G_An(temp_params)
            self.tk_text_mg97ybm0.insert(END, f"共栅放大器的放大系数 A_v = {temp_params.get('An', '未计算出')}\n")
            
            # 共漏放大器
            temp_params = self.params.copy()
            temp_params = calc_shared_D_An(temp_params)
            self.tk_text_mg97ybm0.insert(END, f"共漏放大器的放大系数 A_v = {temp_params.get('An', '未计算出')}\n")
            
            # 显示关键参数
            self.tk_text_mg97ybm0.insert(END, "\n关键参数摘要：\n")
            key_params = ['fet_type', 'I_DSS', 'U_GSoff', 'U_GSth', 'λ', 'R_S', 'R_D', 'R_L', 'gm','workspace']
            for key in key_params:
                if key in self.params:
                    self.tk_text_mg97ybm0.insert(END, f"{key}: {self.params[key]}\n")
        except Exception as e:
            self.tk_text_mg97ybm0.delete(1.0, END)
            self.tk_text_mg97ybm0.insert(END, f"计算过程中发生错误：{str(e)}")
        
    def show_characteristic_curve(self):
        """显示特性曲线"""
        self.read_input_values()
        # 使用ShowDiagram类显示特性曲线
        self.diagram.show_characteristic_curve(self.params)
        
    def clear_characteristic_curve(self):
        """清空特性曲线"""
        self.tk_canvas_mg97v16m.delete("all")
        self.tk_canvas_mg97w0hx.delete("all")
        self.diagram.clear()
        
    def show_graphical_method(self):
        """显示图解法"""
        self.read_input_values()
        # 使用ShowDiagram类显示图解法结果
        self.diagram.show_graphical_method(self.params)

class Win(WinGUI):
    def __init__(self, controller=None):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        if self.ctl:
            self.ctl.init(self)
            
    def __event_bind(self):
        # 这里可以添加额外的事件绑定
        pass
        
    def __style_config(self):
        # 这里可以添加样式配置
        pass