from tkinter import *
from tkinter.ttk import *

class ButtonComponents:
    """按钮组件类"""
    
    @staticmethod
    def create_calculate_id_button(parent):
        """创建计算漏极电流按钮"""
        btn = Button(parent, text="计算对应I_D", takefocus=False)
        btn.place(x=125, y=50, width=90, height=30)
        return btn
        
    @staticmethod
    def create_calculate_amplifier_button(parent):
        """创建计算放大系数按钮"""
        btn = Button(parent, text="计算放大系数", takefocus=False)
        btn.place(x=125, y=90, width=90, height=30)
        return btn
        
    @staticmethod
    def create_show_characteristic_curve_button(parent):
        """创建显示特性曲线按钮"""
        btn = Button(parent, text="显示特性曲线", takefocus=False)
        btn.place(x=610, y=510, width=120, height=30)
        return btn
        
    @staticmethod
    def create_clear_characteristic_curve_button(parent):
        """创建清空特性曲线按钮"""
        btn = Button(parent, text="清空特性曲线", takefocus=False)
        btn.place(x=740, y=510, width=120, height=30)
        return btn
        
    @staticmethod
    def create_show_graphical_method_button(parent):
        """创建显示图解法按钮"""
        btn = Button(parent, text="显示图解法", takefocus=False)
        btn.place(x=870, y=510, width=120, height=30)
        return btn
        
    @staticmethod
    def create_calculate_all_button(parent):
        """创建计算全部按钮"""
        btn = Button(parent, text="计算全部", takefocus=False)
        btn.place(x=355, y=510, width=150, height=30)
        return btn