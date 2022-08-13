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
import random

x = [0] # x represent mRNA
t = [0] # t represnt time point 

tend = 1000 # simulation end time

k = 2 # production rate
gamma = 0.1 # degradation rate

while t[-1] < tend:
    current_x = x[-1] # gives latest value of x
    rates = [k, gamma * current_x]
    rate_sum = sum(rates)
    tau = np.random.exponential(scale=1/rate_sum) # tau is the time points for next event
    t.append(t[-1] + tau)
    rand = random.uniform(0,1)
    if rand * rate_sum > 0 and rand * rate_sum < rates[0]:# production event
            x.append(x[-1] + 1)
    elif rand * rate_sum > rates[0] and rand * rate_sum < rates[0] + rates[1]:# decay event
            x.append(x[-1] - 1)plt.plot(t,x)
            
plt.xlabel("time")
plt.ylabel("mRNA quantity")
#plt.show()
plt.savefig("gillespie_algoritm_1.pdf", dpi=400,  bbox_inches='tight')
            
