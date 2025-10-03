from tkinter import *
from tkinter.ttk import *

class InputComponents:
    """输入框组件类"""
    
    @staticmethod
    def create_idss_input(parent):
        """创建I_DSS输入框"""
        ipt = Entry(parent)
        ipt.place(x=120, y=25, width=50, height=30)
        return ipt
        
    @staticmethod
    def create_phi_g_input(parent):
        """创建ϕ_G输入框"""
        ipt = Entry(parent)
        ipt.place(x=220, y=25, width=50, height=30)
        return ipt
        
    @staticmethod
    def create_phi_s_input(parent):
        """创建ϕ_S输入框"""
        ipt = Entry(parent)
        ipt.place(x=320, y=25, width=50, height=30)
        return ipt
        
    @staticmethod
    def create_phi_d_input(parent):
        """创建ϕ_D输入框"""
        ipt = Entry(parent)
        ipt.place(x=420, y=25, width=50, height=30)
        return ipt
        
    @staticmethod
    def create_vgsoff_input(parent):
        """创建U_GSoff输入框"""
        ipt = Entry(parent)
        ipt.place(x=140, y=60, width=50, height=30)
        return ipt
        
    @staticmethod
    def create_vgsth_input(parent):
        """创建U_GSth输入框"""
        ipt = Entry(parent)
        ipt.place(x=265, y=60, width=50, height=30)
        return ipt
        
    @staticmethod
    def create_lambda_input(parent):
        """创建λ输入框"""
        ipt = Entry(parent)
        ipt.place(x=615, y=50, width=50, height=30)
        return ipt
        
    @staticmethod
    def create_rg_input(parent):
        """创建R_G输入框"""
        ipt = Entry(parent)
        ipt.place(x=120, y=95, width=50, height=30)
        return ipt
        
    @staticmethod
    def create_rs_input(parent):
        """创建R_S输入框"""
        ipt = Entry(parent)
        ipt.place(x=220, y=95, width=50, height=30)
        return ipt
        
    @staticmethod
    def create_rd_input(parent):
        """创建R_D输入框"""
        ipt = Entry(parent)
        ipt.place(x=320, y=95, width=50, height=30)
        return ipt
        
    @staticmethod
    def create_rl_input(parent):
        """创建R_L输入框"""
        ipt = Entry(parent)
        ipt.place(x=420, y=95, width=50, height=30)
        return ipt
        
    @staticmethod
    def create_gm_input(parent):
        """创建gm输入框"""
        ipt = Entry(parent)
        ipt.place(x=620, y=95, width=50, height=30)
        return ipt
        
    @staticmethod
    def create_kn_input(parent):
        """创建Kn输入框"""
        ipt = Entry(parent)
        ipt.place(x=390, y=60, width=50, height=30)
        return ipt