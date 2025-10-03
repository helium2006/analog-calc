'''N沟道增强型MOSFET,输入params字典，包含G,S,D三极电势,Vth,Kn=k*W/L,λ(可选)'''
from fet_calc.utils.data_process.check.check_workspace import add_fet_workspace ,check_fet_workspace
from fet_calc.utils.data_process.calc.calc_voltage import calc_voltage

def enhanced_N_channel_mosfet_without_lambda(params:dict):
    ϕ_S = params['ϕ_S']
    ϕ_G = params['ϕ_G']
    ϕ_D = params['ϕ_D']
    U_GSth = params['U_GSth']
    Kn = params['Kn']
    
    U_GS=calc_voltage(ϕ_G,ϕ_S)  # 计算栅源电压
    U_DS=calc_voltage(ϕ_D,ϕ_S)  # 计算漏源电压
    U_GD=calc_voltage(ϕ_G,ϕ_D)  # 计算栅漏电压
    
    fet_type = 'enhanced_N_channel_mosfet'
    params.update({'U_GS':U_GS,'U_DS':U_DS,'U_GD':U_GD,'fet_type':fet_type,'U_GSth':U_GSth})
    params=add_fet_workspace(params)  # 添加工作区域
    
    workspace=check_fet_workspace(params)  # 检查工作区域
    if workspace == '截止区':
        ID = 0
    elif workspace == '线性区':
        ID = Kn * ((U_GS - U_GSth) * U_DS - U_DS ** 2 / 2)
    elif workspace == '饱和区':
        ID = Kn * (U_GS - U_GSth) ** 2 / 2
    params['ID']=ID
    return params   

def enhanced_N_channel_mosfet_with_lambda(params:dict):
    ϕ_S = params['ϕ_S']
    ϕ_G = params['ϕ_G']
    ϕ_D = params['ϕ_D']
    U_GSth = params['U_GSth']
    Kn = params['Kn']
    λ = params['λ']
    
    U_GS=calc_voltage(ϕ_G,ϕ_S)  # 计算栅源电压
    U_DS=calc_voltage(ϕ_D,ϕ_S)  # 计算漏源电压
    U_GD=calc_voltage(ϕ_G,ϕ_D)  # 计算栅漏电压
    
    fet_type = 'enhanced_N_channel_mosfet'
    params.update({'U_GS':U_GS,'U_DS':U_DS,'U_GD':U_GD,'fet_type':fet_type,'U_GSth':U_GSth,'λ':λ})
    params=add_fet_workspace(params)  # 添加工作区域
    
    workspace=check_fet_workspace(params)  # 检查工作区域
    if workspace == '截止区':
        ID = 0
    elif workspace == '线性区':
        ID = Kn * ((U_GS - U_GSth) * U_DS - U_DS ** 2 / 2) * (1 + λ * U_DS)
    elif workspace == '饱和区':
        ID = Kn * (U_GS - U_GSth) ** 2 / 2 * (1 + λ * U_DS)
    params['ID']=ID
    return params