'''接受计算的参数，返回求解的根'''
import cmath
def solve_quadratic_equation(coefficient:dict):
    solution={}
    a = coefficient['a']
    b = coefficient['b']
    c = coefficient['c']
    d = (b**2) - (4*a*c)
    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)
    solution.update({'root1': root1.real, 'root2': root2.real})
    return solution