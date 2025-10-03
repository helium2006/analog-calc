from tkinter import *
from tkinter.ttk import *

class LabelComponents:
    """标签组件类"""
    
    @staticmethod
    def create_fet_type_label(parent):
        """创建FET类型选择标签"""
        label = Label(parent, text="选择fet类型", anchor="center")
        label.place(x=10, y=10, width=96, height=30)
        return label
        
    @staticmethod
    def create_dc_mode_label(parent):
        """创建直流模式选择标签"""
        label = Label(parent, text="选择直流模式", anchor="center")
        label.place(x=10, y=10, width=115, height=30)
        return label
        
    @staticmethod
    def create_amplifier_label(parent):
        """创建放大电路结构选择标签"""
        label = Label(parent, text="选择放大电路结构", anchor="center")
        label.place(x=10, y=10, width=120, height=30)
        return label
        
    @staticmethod
    def create_params_label(parent):
        """创建参数输入标签"""
        label = Label(parent, text="输入参数:", anchor="center")
        label.place(x=10, y=10, width=60, height=30)
        return label
        
    @staticmethod
    def create_idss_label(parent):
        """创建I_DSS标签"""
        label = Label(parent, text="I_DSS:", anchor="center")
        label.place(x=75, y=25, width=40, height=30)
        return label
        
    @staticmethod
    def create_phi_g_label(parent):
        """创建ϕ_G标签"""
        label = Label(parent, text="ϕ_G:", anchor="center")
        label.place(x=175, y=25, width=40, height=30)
        return label
        
    @staticmethod
    def create_phi_s_label(parent):
        """创建ϕ_S标签"""
        label = Label(parent, text="ϕ_S:", anchor="center")
        label.place(x=275, y=25, width=40, height=30)
        return label
        
    @staticmethod
    def create_phi_d_label(parent):
        """创建ϕ_D标签"""
        label = Label(parent, text="ϕ_D:", anchor="center")
        label.place(x=375, y=25, width=40, height=30)
        return label
        
    @staticmethod
    def create_vgsoff_label(parent):
        """创建U_GSoff标签"""
        label = Label(parent, text="U_GSoff:", anchor="center")
        label.place(x=75, y=60, width=60, height=30)
        return label
        
    @staticmethod
    def create_vgsth_label(parent):
        """创建U_GSth标签"""
        label = Label(parent, text="U_GSth:", anchor="center")
        label.place(x=200, y=60, width=60, height=30)
        return label
        
    @staticmethod
    def create_lambda_label(parent):
        """创建λ标签"""
        label = Label(parent, text="λ:", anchor="center")
        label.place(x=580, y=50, width=20, height=30)
        return label
        
    @staticmethod
    def create_rg_label(parent):
        """创建R_G标签"""
        label = Label(parent, text="R_G:", anchor="center")
        label.place(x=75, y=95, width=40, height=30)
        return label
        
    @staticmethod
    def create_rs_label(parent):
        """创建R_S标签"""
        label = Label(parent, text="R_S:", anchor="center")
        label.place(x=175, y=95, width=40, height=30)
        return label
        
    @staticmethod
    def create_rd_label(parent):
        """创建R_D标签"""
        label = Label(parent, text="R_D:", anchor="center")
        label.place(x=275, y=95, width=40, height=30)
        return label
        
    @staticmethod
    def create_rl_label(parent):
        """创建R_L标签"""
        label = Label(parent, text="R_L:", anchor="center")
        label.place(x=375, y=95, width=40, height=30)
        return label
        
    @staticmethod
    def create_gm_label(parent):
        """创建gm标签"""
        label = Label(parent, text="gm:", anchor="center")
        label.place(x=579, y=95, width=30, height=30)
        return label
        
    @staticmethod
    def create_resistor_unit_label(parent):
        """创建电阻单位标签"""
        label = Label(parent, text="电阻单位:", anchor="center")
        label.place(x=15, y=45, width=55, height=30)
        return label
        
    @staticmethod
    def create_kn_label(parent):
        """创建Kn标签"""
        label = Label(parent, text="Kn:", anchor="center")
        label.place(x=325, y=60, width=60, height=30)
        return label