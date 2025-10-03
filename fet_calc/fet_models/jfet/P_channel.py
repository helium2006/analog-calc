'''P沟道JFET模型，输入params字典，包含S,G,D三极电势、I_DSS和U_GSoff，输出D极电流ID'''

from fet_calc.utils.data_process.check.check_workspace import add_fet_workspace , check_fet_workspace
from fet_calc.utils.data_process.calc.calc_voltage import calc_voltage

def P_channel_jfet(params:dict):
    ϕ_S = params['ϕ_S']
    ϕ_G = params['ϕ_G']
    ϕ_D = params['ϕ_D']
    I_DSS = params['I_DSS']
    U_GSoff = params['U_GSoff']
    
    U_GS=calc_voltage(ϕ_G, ϕ_S)  # 计算栅源电压
    U_DS=calc_voltage(ϕ_D, ϕ_S)  # 计算漏源电压
    U_GD=calc_voltage(ϕ_G, ϕ_D)  # 计算栅漏电压
    
    fet_type = 'P_channel_jfet'

    params.update({'U_GS':U_GS,'U_DS':U_DS,'U_GD':U_GD,'fet_type':fet_type,'U_GSoff':U_GSoff})
    params=add_fet_workspace(params)  # 添加工作区域
    
    workspace=check_fet_workspace(params)  # 检查工作区域
    if workspace == '截止区':
        ID = 0
    elif workspace == '线性区':
        ID = I_DSS * (1 - U_GS / U_GSoff) ** 2 * (1 - U_DS / (U_GS - U_GSoff))
    elif workspace == '饱和区':
        ID = I_DSS * (1 - U_GS / U_GSoff) ** 2
    params['ID']=ID
    return params