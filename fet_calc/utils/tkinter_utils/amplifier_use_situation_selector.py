'''接受从tkinter返回的params，根据amplifier_situation选择不同的计算函数'''
from fet_calc.utils.fet_using_situations.amplifer_use.shared_S import calc_shared_S_An
from fet_calc.utils.fet_using_situations.amplifer_use.shared_G import calc_shared_G_An
from fet_calc.utils.fet_using_situations.amplifer_use.shared_D import calc_shared_D_An
def amplifier_use_situation_selector(params:dict) -> dict:
    '''根据amplifier_situation选择不同的计算函数'''
    amplifier_situation=params.get("amplifier_situation", None)
    if amplifier_situation is None:
        return params
    if amplifier_situation == "shared_S":
        params=calc_shared_S_An(params)
    elif amplifier_situation == "shared_G":
        params=calc_shared_G_An(params)
    elif amplifier_situation == "shared_D":
        params=calc_shared_D_An(params)
    else:
        return params
    return params
