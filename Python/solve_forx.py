# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 12:32:27 2018

@author: hithr
"""

#%% 
# solve for x based on mean
from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
print(solve(16 + 42 + 9*x - 6.95*(11 + x), x))
print(solve(6*(-2*x-1)+ 13*x +2, x))
print(solve(x - 4 -21, x))
print(solve(3 - x - 2*(9 + 2*x), x))
#%%
# expect value for discrete variables
print((0*10 + 1*64 + 2*42 + 3*84)/200)

