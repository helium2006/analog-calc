def check_valid_root(solution:dict,params:dict):
    root1 = solution['root1']
    root2 = solution['root2']
    I_DSS = params['I_DSS']
    fet_type = params['fet_type']
    possible_root=min(root1,root2)
    if fet_type in ['N_channel_jfet','N_channel_mosfet_depletion','N_channel_mosfet_enhanced']:
        if possible_root >=0 and possible_root <= I_DSS:
            valid_root=possible_root
        else:
            valid_root=None
    elif fet_type in ['P_channel_jfet','P_channel_mosfet_depletion','P_channel_mosfet_enhanced']:
        if possible_root <=0 and possible_root >= -I_DSS:
            valid_root=possible_root
        else:
            valid_root=None
    params['valid_root']=valid_root
    return params
   