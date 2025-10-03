def calc_parallel_resistor(R1,R2):
    '''计算并联电阻'''
    if R1 ==0 or R2 ==0:
        return max(R1,R2)   
    else:   
        return 1/(1/R1+1/R2)    