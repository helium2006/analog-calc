'''计算共栅放大器放大系数'''
from fet_calc.utils.data_process.calc.calc_gm import calc_fet_gm

def calc_shared_G_An(params:dict) :
    '''计算共栅放大器放大系数'''
    gm=params.get("gm", None)
    if gm is 0.0:
        params=calc_fet_gm(params)
        gm=params.get("gm", None)
    RS=params.get("RS", None)
    RD=params.get("RD", None)
    An=(gm*RD)/(1+gm*RS)
    params["An"]=An
    return params