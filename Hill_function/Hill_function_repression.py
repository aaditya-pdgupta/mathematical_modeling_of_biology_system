
# We need some modules (Python libraries) in the following.
# Usually, such modules are loaded in the first cell of a notebook.
# The modules that we need concern numerical calculations,
# solving the ordinary differential equations, and plotting them later.

# all plots should appear directly within the notebook
%matplotlib inline

# modules necessary for plotting
import matplotlib.pyplot as plt

# integrate a system of ordinary differential equations
# initial value problem
from scipy.integrate import odeint

# module to make available data structures and routines
# for numerics
import numpy as np

# 0 for G1 and 0 for G2
y0 = [0,0] 
# 100 means hundred different point
t = np.linspace(0,200,num=100) 

 #degradtion rate should be less than production rate
k_1 = 0.5
gamma_1 = 0.1
k_2 = 0.5
gamma_2 = 0.05
n = 5
c = 5

#putting the params to array which will be passed in this offer
params = [k_1, gamma_1, k_2, gamma_2, n, c] 

def repression(variables, t, params):
    #they are the first, second and so on element of the params
    #and arraygamma_m = params[1]
    G1 = variables[0]
    G2 = variables[1]
    k_1 = params[0]
    gamma_1 = params[1]
    k_2 = params[2]
    gamma_2 = params[3]
    n = params[4]
    c = params[5]
    dG1dt = k_1 - gamma_1 * G1
    dG2dt = (c**n / (c**n + G1**n)) * k_2 - gamma_2 * G2
    return([dG1dt,dG2dt])

#, is used for storing args and we get y matrix with two column one for G1
# and another for G2 and row for every time point  
y = odeint(repression, y0, t, args=(params,)) 

plt.plot(t , y[:,0], color="b", label="G1")
plt.plot(t , y[:,1], color="r", label="G2")
plt.xlabel("Time")
plt.ylabel("Number")
plt.legend()
plt.grid()
plt.show()
