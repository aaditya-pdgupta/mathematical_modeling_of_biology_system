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
        # gives latest value of x
    current_x = x[-1] 
    rates = [k, gamma * current_x]
    rate_sum = sum(rates)
    # tau is the time points for next event
    tau = np.random.exponential(scale=1/rate_sum) 
    t.append(t[-1] + tau)
    rand = random.uniform(0,1)
    # production event
    if rand * rate_sum > 0 and rand * rate_sum < rates[0]:
            x.append(x[-1] + 1)
        # production event
    elif rand * rate_sum > rates[0] and rand * rate_sum < rates[0] + rates[1]:
            x.append(x[-1] - 1)plt.plot(t,x)
            
plt.xlabel("time")
plt.ylabel("mRNA quantity")
plt.show()

            
