def basic_use(params:dict):
    fet_type = params['fet_type']
    λ=params.get('λ',0)  # 默认为0
    print(params)
    print('ϕ_S:',params['ϕ_S'])
    if fet_type in ['N_channel_jfet','P_channel_jfet']:
        from fet_calc.fet_models.jfet.N_channel import N_channel_jfet
        from fet_calc.fet_models.jfet.P_channel import P_channel_jfet
        if fet_type == 'N_channel_jfet':
            params=N_channel_jfet(params)
        elif fet_type == 'P_channel_jfet':
            params=P_channel_jfet(params)
    elif fet_type in ['N_channel_mosfet_depletion','P_channel_mosfet_depletion']:
        if λ == 0:
            from fet_calc.fet_models.mosfet.depletion.N_channel import depletion_N_channel_mosfet_without_lambda
            from fet_calc.fet_models.mosfet.depletion.P_channel import depletion_P_channel_mosfet_without_lambda
            if fet_type == 'N_channel_mosfet_depletion':
                params=depletion_N_channel_mosfet_without_lambda(params)
            elif fet_type == 'P_channel_mosfet_depletion':
                params=depletion_P_channel_mosfet_without_lambda(params)
        else:
            from fet_calc.fet_models.mosfet.depletion.N_channel import depletion_N_channel_mosfet_with_lambda
            from fet_calc.fet_models.mosfet.depletion.P_channel import depletion_P_channel_mosfet_with_lambda
            if fet_type == 'N_channel_mosfet_depletion':
                params=depletion_N_channel_mosfet_with_lambda(params)
            elif fet_type == 'P_channel_mosfet_depletion':
                params=depletion_P_channel_mosfet_with_lambda(params)
    elif fet_type in ['N_channel_mosfet_enhanced','P_channel_mosfet_enhanced']:
        if λ == 0:
            from fet_calc.fet_models.mosfet.enhanced.N_channel import enhanced_N_channel_mosfet_without_lambda
            from fet_calc.fet_models.mosfet.enhanced.P_channel import enhanced_P_channel_mosfet_without_lambda
            if fet_type == 'N_channel_mosfet_enhanced':
                params=enhanced_N_channel_mosfet_without_lambda(params)
            elif fet_type == 'P_channel_mosfet_enhanced':
                params=enhanced_P_channel_mosfet_without_lambda(params)
        else:
            from fet_calc.fet_models.mosfet.enhanced.N_channel import enhanced_N_channel_mosfet_with_lambda
            from fet_calc.fet_models.mosfet.enhanced.P_channel import enhanced_P_channel_mosfet_with_lambda
            if fet_type == 'N_channel_mosfet_enhanced':
                params=enhanced_N_channel_mosfet_with_lambda(params)
            elif fet_type == 'P_channel_mosfet_enhanced':
                params=enhanced_P_channel_mosfet_with_lambda(params)
    params['I_D_basic_use']=params['ID']  # 将计算得到的ID存入I_D_basic_use
    return params
    