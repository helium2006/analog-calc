'''计算共漏放大器放大系数'''
from fet_calc.utils.data_process.calc.calc_gm import calc_fet_gm
from fet_calc.utils.data_process.calc.calc_parallel_resistor import calc_parallel_resistor
def calc_shared_D_An(params:dict) :
    '''计算共漏放大器放大系数'''
    gm=params.get("gm", None)
    if gm is 0.0:
        params=calc_fet_gm(params)
        gm=params.get("gm", None)
    RS=params.get("RS", None)
    RL=params.get('RL',None)
    RL0=calc_parallel_resistor(RL,RS)
    An=(gm*RL0)/(1+gm*RL0)
    params["An"]=An
    return params
