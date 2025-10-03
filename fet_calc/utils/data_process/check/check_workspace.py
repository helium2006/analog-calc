'''判断fet管的工作区域'''
def add_fet_workspace(params:dict):
    U_GS = params['U_GS']
    U_DS = params['U_DS']
    U_GD = params['U_GD']
    
    fet_type = params['fet_type']
    
    # N沟道JFET
    if fet_type == 'N_channel_jfet':
        U_GSoff = params['U_GSoff']  # 对于N沟道JFET，U_GSoff通常是负值
        if U_GS <= U_GSoff:  # 当栅源电压小于等于夹断电压时，JFET截止
            workspace = '截止区'
        elif U_GSoff<U_GS and U_GS < 0 and U_GD<U_GSoff:  
            workspace = '饱和区'
        elif U_GSoff<U_GS and U_GS < 0 and U_GSoff < U_GD:  
            workspace = '线性区'
        else:
            workspace = None
    
    # P沟道JFET
    elif fet_type == 'P_channel_jfet':
        U_GSoff = params['U_GSoff']  # 对于P沟道JFET，U_GSoff通常是正值
        if U_GS > U_GSoff:  # 当栅极电压高于夹断电压时，JFET截止
            workspace = '截止区'
        elif 0<U_GS and U_GS < U_GSoff and U_GD < U_GSoff:  
            workspace = '饱和区'
        elif 0< U_GS and U_GS < U_GSoff and 0<U_GD and U_GD < U_GSoff:  
            workspace = '线性区'
        else:
            workspace = None
    
    # 增强型N沟道MOSFET
    elif fet_type == 'enhanced_N_channel_mosfet':
        U_GSth = params['U_GSth']  # 对于增强型N沟道MOSFET，U_GSth通常是正值
        if U_GS <= U_GSth:  # 当栅源电压小于阈值电压时，处于截止区
            workspace = '截止区'
        elif U_GSth <U_GS and U_GSth < U_GD:  
            workspace = '线性区'
        elif U_GSth < U_GS and U_GD < U_GSth:  
            workspace = '饱和区' 
    
    # 增强型P沟道MOSFET
    elif fet_type == 'enhanced_P_channel_mosfet':
        U_GSth = params['U_GSth']  # 对于增强型P沟道MOSFET，U_GSth通常是负值
        if U_GS >= U_GSth:  # 当栅源电压大于阈值电压时，处于截止区
            workspace = '截止区'
        elif U_GS < U_GSth and U_GSth < U_GD:   
            workspace = '饱和区'
        elif U_GS < U_GSth and U_GD < U_GSth:  
            workspace = '线性区'
    
    # 耗尽型N沟道MOSFET
    elif fet_type == 'depletion_N_channel_mosfet':
        U_GSoff = params['U_GSoff']  # 对于耗尽型N沟道MOSFET，U_GSoff通常是负值
        if U_GS < U_GSoff:  # 当栅极电压低于夹断电压时，处于截止区
            workspace = '截止区'
        elif U_GSoff < U_GS and U_GD < U_GSoff:  
            workspace = '饱和区'
        elif U_GSoff < U_GS  and U_GSoff < U_GD:  
            workspace = '线性区' 
        else:
            workspace = None

    # 耗尽型P沟道MOSFET
    elif fet_type == 'depletion_P_channel_mosfet':
        U_GSoff = params['U_GSoff']  # 对于耗尽型P沟道MOSFET，U_GSoff通常是正值
        if U_GS > U_GSoff:  # 当栅极电压为负或零时，可能处于截止区
            workspace = '截止区'
        elif U_GS < U_GSoff and U_GD > U_GSoff:  
            workspace = '饱和区'
        elif U_GS < U_GSoff and U_GD < U_GSoff:  
            workspace = '线性区' 
        else:
            workspace = None
    else:
        workspace = None
    params['workspace'] = workspace
    return params
def check_fet_workspace(params:dict):
    workspace=params.get('workspace',None)
    return workspace