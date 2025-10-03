from fet_calc.utils.fet_using_situations.DC_use.basic_use import basic_use
from fet_calc.utils.fet_using_situations.DC_use.DC_self_bia import calc_I_D_DC_self_bia
from fet_calc.utils.fet_using_situations.DC_use.DC_div_voltage_bia import calc_I_D_DC_div_voltage_bia

'''计算跨导并存入params'''
def get_true_ID(params:dict):
    '''读取当前工作状态的漏极电流'''
    use_situation=params.get("DC_use_situation", None)
    if use_situation is not None:
        if 'self_bia' in use_situation.lower():
            ID=params.get("I_D_DC_self_bia", None)
        elif 'div_voltage_bia' in use_situation.lower():
            ID=params.get("I_D_DC_div_voltage_bia", None)
        else:
            ID=params.get("I_D_basic_use", None)
    else:
        ID=params.get("I_D_DC_div_voltage_bia", None) #放大电路一般使用分压偏置
    if ID is None:
        ID_params=check_ID(params)
        if 'self_bia' in use_situation.lower():
            ID=ID_params.get("I_D_DC_self_bia")
        elif 'div_voltage_bia' in use_situation.lower():
            ID=ID_params.get("I_D_DC_div_voltage_bia")
        else:
            ID=ID_params.get("I_D_basic_use")
    if ID is None:
        ID=0
    return ID

def calc_fet_gm(params:dict) :
    '''计算跨导，并存入params'''
    fet_type=params.get("fet_type", None)
    if 'enhanced' in fet_type.lower():
        ID=get_true_ID(params)
        Kn=params.get("Kn", None)
        gm=(2*Kn*ID)**0.5
        params["gm"]=gm
    elif 'depleted' in fet_type.lower() or 'jfet' in fet_type.lower():
        ID=get_true_ID(params)
        U_GS=params.get("U_GS", None)
        U_GSoff=params.get("U_GSoff", None)
        if ID is not None and U_GS is not None and U_GSoff is not None:
            gm=2*ID/(U_GS-U_GSoff)
        else:
            gm=None
            raise ValueError("缺少必要参数，无法计算")
        params["gm"]=gm
    else:
        params["gm"]=None
        raise ValueError("不支持的fet类型")
    return params

def check_ID(params:dict) -> dict:
    temp_params={}
    check_basic_use_ID=params.get('I_D_basic_use',0)
    check_DC_self_bia=params.get('I_D_DC_self_bia',0)
    check_DC_div_voltage_bia=params.get('I_D_DC_div_voltage_bia',0)
    if check_basic_use_ID==0 or check_DC_self_bia==0 or check_DC_div_voltage_bia==0:
        try:
            temp_params['ID']=basic_use(params)
            temp_params['I_D_basic_use']=temp_params['ID']
            temp_params['I_D_DC_self_bia']=calc_I_D_DC_self_bia(params)
            temp_params['I_D_DC_div_voltage_bia']=calc_I_D_DC_div_voltage_bia(params)
        except Exception as e:
           pass