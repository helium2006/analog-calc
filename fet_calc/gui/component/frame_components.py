from tkinter import *
from tkinter.ttk import *

class FrameComponents:
    """框架组件类"""
    
    @staticmethod
    def create_fet_type_frame(parent):
        """创建FET类型选择框架"""
        frame = Frame(parent,)
        frame.place(x=10, y=10, width=230, height=300)
        return frame
        
    @staticmethod
    def create_dc_mode_frame(parent):
        """创建直流模式选择框架"""
        frame = Frame(parent,)
        frame.place(x=10, y=320, width=230, height=170)
        return frame
        
    @staticmethod
    def create_amplifier_frame(parent):
        """创建放大电路结构选择框架"""
        frame = Frame(parent,)
        frame.place(x=10, y=500, width=230, height=170)
        return frame
        
    @staticmethod
    def create_params_frame(parent):
        """创建参数输入框架"""
        frame = Frame(parent,)
        frame.place(x=250, y=10, width=740, height=150)
        return frame