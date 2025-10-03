from tkinter import *
from tkinter.ttk import *

class CanvasComponents:
    """画布和文本框组件类"""
    
    @staticmethod
    def create_characteristic_curve_canvas(parent):
        """创建特性曲线画布"""
        canvas = Canvas(parent, bg="#aaa")
        canvas.place(x=250, y=180, width=360, height=320)
        return canvas
        
    @staticmethod
    def create_graphical_method_canvas(parent):
        """创建图解法画布"""
        canvas = Canvas(parent, bg="#aaa")
        canvas.place(x=630, y=180, width=360, height=320)
        return canvas
        
    @staticmethod
    def create_result_text(parent):
        """创建结果显示文本框"""
        text = Text(parent)
        text.place(x=250, y=570, width=740, height=100)
        return text