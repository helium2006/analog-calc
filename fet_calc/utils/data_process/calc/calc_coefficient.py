'''计算在不同的fet使用情形下需要求解的二次方程的系数一般只有直流自给式和直流分压式需要计算'''

def calc_coefficient_without_lambda(params:dict):
    """计算不考虑沟道调制效应时的二次方程系数"""
    fet_type = params['fet_type']
    using_situation = params['DC_use_situation']
    a,b,c=0,0,0
    coefficient = {'a':a, 'b':b, 'c':c} 
    
    if using_situation == 'DC_self_bia':
        if 'jfet' in fet_type.lower():
        # JFET的电流方程：ID = I_DSS * (1 - UGS / U_GSoff)^2
        # 联立方程：UGS = -ID * RS 和 ID = I_DSS * (1 - UGS / U_GSoff)^2
        # 代入后得到：ID = I_DSS * (1 + ID * RS / U_GSoff)^2
        # 展开并整理为标准二次方程
            I_DSS = params.get('I_DSS')
            RS = params.get('RS')
            U_GSoff = params.get('U_GSoff')
            print(I_DSS, RS, U_GSoff,type(I_DSS),type(RS),type(U_GSoff))
            print(params)
            a = I_DSS * RS**2 / U_GSoff**2
            b = 2 * I_DSS * RS / U_GSoff - 1
            c = I_DSS
            coefficient = {'a':a, 'b':b, 'c':c}
        elif 'depletion' in fet_type.lower():
        # 耗尽型MOSFET的电流方程：ID = Kn * (UGS - U_GSoff)^2 / 2
        # 联立方程：UGS = -ID * RS 和 ID = Kn * (UGS - U_GSoff)^2 / 2
        # 展开并整理为标准二次方程
            Kn = params.get('Kn')
            RS = params.get('RS')
            U_GSoff = params.get('U_GSoff')
        
            a = Kn * RS**2 / 2
            b = Kn * RS * U_GSoff - 1
            c = Kn * U_GSoff**2 / 2
            coefficient = {'a':a, 'b':b, 'c':c}
        elif 'enhanced' in fet_type.lower():
        # 增强型MOSFET的电流方程：ID = Kn * (UGS - Uth)^2 / 2
        # 联立方程：UGS = -ID * RS 和 ID = Kn * (UGS - Uth)^2 / 2
        # 展开并整理为标准二次方程
            Kn = params.get('Kn')
            RS = params.get('RS')
            U_GSth = params.get('U_GSth')
        
            a = Kn * RS**2 / 2
            b = Kn * RS * U_GSth - 1
            c = Kn * U_GSth**2 / 2
            coefficient = {'a':a, 'b':b, 'c':c}
        else:
            raise ValueError(f'不支持的FET类型: {fet_type}在{using_situation}下的系数计算')
    elif using_situation == 'DC_div_voltage_bia':
        if 'jfet' in fet_type.lower():
        # JFET的电流方程：ID = I_DSS * (1 - UGS / U_GSoff)^2
        # 联立方程：UGS = phi_G - ID * RS 和 ID = I_DSS * (1 - UGS / U_GSoff)^2
        # 代入后得到：ID = I_DSS * (1 - (phi_G - ID * RS) / U_GSoff)^2
        # 展开并整理为标准二次方程
            I_DSS = params.get('I_DSS')
            RS = params.get('RS')
            U_GSoff = params.get('U_GSoff')
            ϕ_G = params.get('ϕ_G')
        
            a = I_DSS * RS**2 / U_GSoff**2
            b = 2 * I_DSS * (ϕ_G - U_GSoff) * RS / U_GSoff**2 - 1
            c = I_DSS * (1 - ϕ_G / U_GSoff)**2
            coefficient = {'a':a, 'b':b, 'c':c}
        elif 'depletion' in fet_type.lower():
        # 耗尽型MOSFET的电流方程：ID = Kn * (UGS - U_GSoff)^2 / 2
        # 联立方程：UGS = phi_G - ID * RS 和 ID = Kn * (UGS - U_GSoff)^2 / 2
        # 展开并整理为标准二次方程
            Kn = params.get('Kn')
            RS = params.get('RS')
            U_GSoff = params.get('U_GSoff')
            ϕ_G = params.get('ϕ_G')
        
            a = Kn * RS**2 / 2
            b = Kn * RS * (U_GSoff - ϕ_G) - 1
            c = Kn * (ϕ_G - U_GSoff)**2 / 2
            coefficient = {'a':a, 'b':b, 'c':c}
        elif 'enhanced' in fet_type.lower():
        # 增强型MOSFET的电流方程：ID = Kn * (UGS - Uth)^2 / 2
        # 联立方程：UGS = phi_G - ID * RS 和 ID = Kn * (UGS - Uth)^2 / 2
        # 代入后得到：ID = Kn * (phi_G - ID * RS - Uth)^2 / 2
        # 展开并整理为标准二次方程  
            Kn = params.get('Kn')
            RS = params.get('RS')
            U_GSth = params.get('U_GSth')
            ϕ_G = params.get('ϕ_G')
        
            a = Kn * RS**2 / 2
            b = Kn * RS * (U_GSth - ϕ_G) - 1
            c = Kn * (ϕ_G - U_GSth)**2 / 2
            coefficient = {'a':a, 'b':b, 'c':c}
        else:
            raise ValueError(f'不支持的FET类型: {fet_type}在{using_situation}下的系数计算')
    else:
        raise ValueError(f'不支持的使用场景: {using_situation}')
    
    return coefficient

def calc_coefficient_with_lambda(params:dict):
    """计算考虑沟道调制效应时的二次方程系数
    注意：沟道调制效应主要影响饱和区的电流计算，需要在获得初步解后进行修正
    """
    # 首先使用不考虑沟道调制效应的方法计算系数
    coefficient = calc_coefficient_without_lambda(params)
    return coefficient

def calc_coefficient(params:dict):
    """根据是否存在λ参数选择合适的系数计算函数"""
    λ = params.get('λ', 0)
    if not λ:
        return calc_coefficient_without_lambda(params)
    else:
        return calc_coefficient_with_lambda(params)