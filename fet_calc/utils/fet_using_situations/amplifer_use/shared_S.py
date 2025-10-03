'''计算共源放大器放大系数'''
from fet_calc.utils.data_process.calc.calc_gm import calc_fet_gm
from fet_calc.utils.data_process.calc.calc_parallel_resistor import calc_parallel_resistor
def calc_shared_S_An(params:dict) :
    '''计算共源放大器放大系数'''
    gm=params.get("gm", None)
    if gm is 0.0:
        params=calc_fet_gm(params)
        gm=params.get("gm", None)
    RS=params.get("RS", None)
    RD=params.get("RD", None)
    RL=params.get('RL',None)
    An=-(gm*RD)/(1+gm*RS)
    params["An"]=An
    return params