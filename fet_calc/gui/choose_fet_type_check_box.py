'''接受tkinter复选框选择的fet_type，将选择的结果写入params，这是最重要的参数，确定了fet的类型，
才好进行后续的选择和计算
'''

from tkinter import *
from tkinter.ttk import *
from fet_calc.gui.component.radio_button_components import RadioButtonComponents

class ChooseFetTypeCheckBox:
    """选择FET类型的复选框类"""
    
    def __init__(self, parent_frame, params):
        """初始化
        
        Args:
            parent_frame: 父框架
            params: 参数字典，用于存储选择的结果
        """
        self.parent_frame = parent_frame
        self.params = params
        
        # 创建单选按钮组件
        self.p_channel_jfet_rb = RadioButtonComponents.create_p_channel_jfet_rb(parent_frame)
        self.n_channel_jfet_rb = RadioButtonComponents.create_n_channel_jfet_rb(parent_frame)
        self.enhanced_n_channel_mosfet_rb = RadioButtonComponents.create_enhanced_n_channel_mosfet_rb(parent_frame)
        self.enhanced_p_channel_mosfet_rb = RadioButtonComponents.create_enhanced_p_channel_mosfet_rb(parent_frame)
        self.depletion_n_channel_mosfet_rb = RadioButtonComponents.create_depletion_n_channel_mosfet_rb(parent_frame)
        self.depletion_p_channel_mosfet_rb = RadioButtonComponents.create_depletion_p_channel_mosfet_rb(parent_frame)
        
        # 初始化变量
        self.fet_type_var = StringVar()
        
        # 将单选按钮与变量关联
        self.__bind_radio_buttons()
        
        # 绑定事件
        self.__bind_events()
        
    def __bind_radio_buttons(self):
        """将单选按钮与变量绑定"""
        self.p_channel_jfet_rb.config(variable=self.fet_type_var, value='P_channel_jfet')
        self.n_channel_jfet_rb.config(variable=self.fet_type_var, value='N_channel_jfet')
        self.enhanced_n_channel_mosfet_rb.config(variable=self.fet_type_var, value='enhanced_N_channel_mosfet')
        self.enhanced_p_channel_mosfet_rb.config(variable=self.fet_type_var, value='enhanced_p_channel_mosfet')
        self.depletion_n_channel_mosfet_rb.config(variable=self.fet_type_var, value='depletion_N_channel_mosfet')
        self.depletion_p_channel_mosfet_rb.config(variable=self.fet_type_var, value='depletion_P_channel_mosfet')
        
    def __bind_events(self):
        """绑定事件处理函数"""
        self.fet_type_var.trace_add("write", self.on_fet_type_change)
        
    def on_fet_type_change(self, *args):
        """FET类型改变时的处理函数，将结果写入params字典"""
        fet_type = self.fet_type_var.get()
        self.params['fet_type'] = fet_type
        # 可以在这里添加额外的处理逻辑，比如根据选择的FET类型更新其他相关参数
        
    def get_fet_type(self):
        """获取当前选择的FET类型
        
        Returns:
            str: 选择的FET类型
        """
        return self.fet_type_var.get()
        
    def set_fet_type(self, fet_type):
        """设置FET类型
        
        Args:
            fet_type: 要设置的FET类型
        """
        self.fet_type_var.set(fet_type)
        self.params['fet_type'] = fet_type
        
    def get_radio_buttons(self):
        """获取所有的单选按钮
        
        Returns:
            dict: 包含所有单选按钮的字典
        """
        return {
            'P_channel_jfet': self.p_channel_jfet_rb,
            'N_channel_jfet': self.n_channel_jfet_rb,
            'enhanced_N_channel_mosfet': self.enhanced_n_channel_mosfet_rb,
            'enhanced_p_channel_mosfet': self.enhanced_p_channel_mosfet_rb,
            'depletion_N_channel_mosfet': self.depletion_n_channel_mosfet_rb,
            'depletion_P_channel_mosfet': self.depletion_p_channel_mosfet_rb
        }
        
    def enable_all(self):
        """启用所有单选按钮"""
        for rb in self.get_radio_buttons().values():
            rb.config(state=NORMAL)
            
    def disable_all(self):
        """禁用所有单选按钮"""
        for rb in self.get_radio_buttons().values():
            rb.config(state=DISABLED)
            
    def reset(self):
        """重置选择"""
        self.fet_type_var.set('')
        self.params['fet_type'] = ''