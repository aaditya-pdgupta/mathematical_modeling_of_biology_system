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

y0 = [0,0] # 0 protein and 0 mRNA
t = np.linspace(0,200,num=100) # 100 means hundred different point

k_m = 0.2
gamma_m = 0.05 #degradtion rate should be less than production rate
k_p = 0.4
gamma_p = 0.1

#putting the params to array which will be passed in this offer
params = [k_m, gamma_m, k_p, gamma_p] 

def dogma(variables, t, params):
    m = variables[0]
    p = variables[1]
    #they are the first, second and so on element of the params 
    #arraygamma_m = params[1]
    k_m = params[0] 
    k_p = params[2]
    gamma_p = params[3]
    dmdt = k_m - gamma_m * m
    dpdt = k_p * m - gamma_p * p
    return([dmdt,dpdt])
        
#, is used for storing args and we get y matrix with two column one for p
#another for m and row for every time point
y = odeint(dogma, y0, t, args=(params,)) 
plt.plot(t,y[:,0], color="b", label="M")
plt.plot(t,y[:,1], color="r", label="P")
plt.xlabel("Abundance")
plt.ylabel("Time")
plt.legend()
plt.grid()
plt.show()

