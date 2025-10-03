from tkinter import *
from tkinter.ttk import *

class RadioButtonComponents:
    """单选按钮组件类"""
    
    @staticmethod
    def create_p_channel_jfet_rb(parent):
        """创建P沟道JFET单选按钮"""
        rb = Radiobutton(parent, text="P_channel_jfet")
        rb.place(x=10, y=50, width=115, height=30)
        return rb
        
    @staticmethod
    def create_n_channel_jfet_rb(parent):
        """创建N沟道JFET单选按钮"""
        rb = Radiobutton(parent, text="N_channel_jfet")
        rb.place(x=10, y=90, width=115, height=30)
        return rb
        
    @staticmethod
    def create_enhanced_n_channel_mosfet_rb(parent):
        """创建增强型N沟道MOSFET单选按钮"""
        rb = Radiobutton(parent, text="enhanced_N_channel_mosfet")
        rb.place(x=10, y=140, width=210, height=30)
        return rb
        
    @staticmethod
    def create_enhanced_p_channel_mosfet_rb(parent):
        """创建增强型P沟道MOSFET单选按钮"""
        rb = Radiobutton(parent, text="enhanced_p_channel_mosfet")
        rb.place(x=10, y=180, width=210, height=30)
        return rb
        
    @staticmethod
    def create_depletion_n_channel_mosfet_rb(parent):
        """创建耗尽型N沟道MOSFET单选按钮"""
        rb = Radiobutton(parent, text="depletion_N_channel_mosfet")
        rb.place(x=10, y=220, width=210, height=30)
        return rb
        
    @staticmethod
    def create_depletion_p_channel_mosfet_rb(parent):
        """创建耗尽型P沟道MOSFET单选按钮"""
        rb = Radiobutton(parent, text="depletion_P_channel_mosfet")
        rb.place(x=10, y=260, width=210, height=30)
        return rb
        
    @staticmethod
    def create_basic_use_rb(parent):
        """创建基本使用单选按钮"""
        rb = Radiobutton(parent, text="basic_use")
        rb.place(x=10, y=50, width=100, height=30)
        return rb
        
    @staticmethod
    def create_dc_self_bia_rb(parent):
        """创建直流自给偏置单选按钮"""
        rb = Radiobutton(parent, text="DC_self_bia")
        rb.place(x=10, y=90, width=110, height=30)
        return rb
        
    @staticmethod
    def create_dc_div_voltage_bia_rb(parent):
        """创建直流分压偏置单选按钮"""
        rb = Radiobutton(parent, text="DC_div_voltage_bia")
        rb.place(x=10, y=130, width=150, height=30)
        return rb
        
    @staticmethod
    def create_shared_d_rb(parent):
        """创建共漏极单选按钮"""
        rb = Radiobutton(parent, text="shared_D")
        rb.place(x=10, y=50, width=90, height=30)
        return rb
        
    @staticmethod
    def create_shared_g_rb(parent):
        """创建共栅极单选按钮"""
        rb = Radiobutton(parent, text="shared_G")
        rb.place(x=10, y=90, width=90, height=30)
        return rb
        
    @staticmethod
    def create_shared_s_rb(parent):
        """创建共源极单选按钮"""
        rb = Radiobutton(parent, text="shared_S")
        rb.place(x=10, y=130, width=90, height=30)
        return rb
        
    @staticmethod
    def create_lambda_enable_rb(parent):
        """创建启用沟道调制参数单选按钮"""
        rb = Radiobutton(parent, text="启用沟道调制参数")
        rb.place(x=580, y=10, width=150, height=30)
        return rb
        
    @staticmethod
    def create_resistor_unit_kilo_rb(parent):
        """创建千欧电阻单位单选按钮"""
        rb = Radiobutton(parent, text="kΩ")
        rb.place(x=20, y=80, width=50, height=30)
        return rb
        
    @staticmethod
    def create_resistor_unit_mega_rb(parent):
        """创建兆欧电阻单位单选按钮"""
        rb = Radiobutton(parent, text="MΩ")
        rb.place(x=20, y=115, width=50, height=30)
        return rb