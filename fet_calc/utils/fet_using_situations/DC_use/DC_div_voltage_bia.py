'''计算fet在直流分压偏置时的漏极电流并存入params'''
from fet_calc.utils.data_process.calc.calc_coefficient import calc_coefficient
from fet_calc.utils.data_process.math.solve_quadratic_equation import solve_quadratic_equation
from fet_calc.utils.data_process.check.check_valid_root import check_valid_root
from fet_calc.utils.data_process.calc.calc_voltage import calc_voltage

def calc_I_D_DC_div_voltage_bia_without_lambda(params):
    """不考虑沟道调制效应时计算直流分压偏置下的漏极电流"""
    coefficient=calc_coefficient(params)  # 计算系数
    results=solve_quadratic_equation(coefficient)  # 求解二次方程
    params=check_valid_root(results,params)  # 检查有效根并存入params
    valid_root=params['valid_root']
    if valid_root is not None:
        params['I_D_DC_div_voltage_bia']=valid_root  # 将有效根存入params的ID
    else:
        params['I_D_DC_div_voltage_bia']=None  # 无有效根时，ID设为None
    return params

def calc_I_D_DC_div_voltage_bia_with_lambda(params):
    """考虑沟道调制效应时计算直流分压偏置下的漏极电流"""
    # 首先获取不考虑沟道调制效应时的解
    params = calc_I_D_DC_div_voltage_bia_without_lambda(params.copy())
    ID_without_lambda = params.get('I_D_DC_div_voltage_bia')
    
    if ID_without_lambda is not None and ID_without_lambda > 0:
        λ = params.get('λ', 0)
        if λ > 0:
            # 获取必要的参数来计算U_DS
            ϕ_S = params.get('ϕ_S', 0)
            ϕ_D = params.get('ϕ_D', 0)
            # 计算漏源电压U_DS
            U_DS = calc_voltage(ϕ_D, ϕ_S)
            # 应用沟道调制效应修正
            ID_with_lambda = ID_without_lambda * (1 + λ * U_DS)
            params['I_D_DC_div_voltage_bia'] = ID_with_lambda
            # 存储原始值以便比较
            params['I_D_DC_div_voltage_bia_without_lambda'] = ID_without_lambda
    
    return params

def calc_I_D_DC_div_voltage_bia(params):
    """根据是否存在λ参数选择合适的计算函数"""
    λ=params.get('λ',0)  # 默认为0
    if not λ:  # 不考虑沟道调制效应
        return calc_I_D_DC_div_voltage_bia_without_lambda(params)
    else:  # 考虑沟道调制效应
        return calc_I_D_DC_div_voltage_bia_with_lambda(params)