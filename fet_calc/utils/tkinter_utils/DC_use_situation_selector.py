'''接受从tkinter返回的params，根据DC_use_situation选择不同的计算函数'''
from fet_calc.utils.fet_using_situations.DC_use.basic_use import basic_use
from fet_calc.utils.fet_using_situations.DC_use.DC_div_voltage_bia import calc_I_D_DC_div_voltage_bia
from fet_calc.utils.fet_using_situations.DC_use.DC_self_bia import calc_I_D_DC_self_bia
def DC_use_situation_selector(params:dict):
    DC_use_situation=params['DC_use_situation']
    if DC_use_situation=='basic_use':
        params=basic_use(params)        
    elif DC_use_situation=='DC_self_bia':
        params=calc_I_D_DC_self_bia(params)        
    elif DC_use_situation=='DC_div_voltage_bia':
        params=calc_I_D_DC_div_voltage_bia(params)
    else:
        return params   
    return params

          
        