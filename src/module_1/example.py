import numpy as np

def add_pi(a):
    if isinstance(a, int) or isinstance(a, float):
        return a + np.pi
    else:
        return False
    
def cl_f():
    return print('logged to the console from module_1')
