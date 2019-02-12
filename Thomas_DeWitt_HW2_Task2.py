import numpy as np
import math as m
import matplotlib.pyplot as plt


def init():   # function to set initial variables
       global ax, ay, delt, t, x, y  # need to make these exist everywhere
       ax = 0.0
       ay = -9.8           # define the constant acceleration values
       delt = 0.1
       t = 0.0          # define a time scale for the functions to run
       x = [x0]
       y = [y0]            # set initial values

def inputs():     # function to take inputs
       global x0, y0, vx0, vy0           # need to make these exist everywhere
       x0 = float(input('Initial Position x = '))
       y0 = float(input('Initial Position y = '))
       vx0 = float(input('Initial Velocity x = '))
       vy0 = float(input('Initial Velocity y = '))         # Takes input for initial values

def px(x,v,time,a):    # Function to calculate values
    return x + v*time + 0.5*a*time**2

def plot_data():
       t = 0    # set initial value locally
       while y[-1] >= 0:    # Does this until the last value in y is less that 0
              x.append(px(x0,vx0,t,ax)) #  Creates a tuple of calculated values, like coordinates
              y.append(px(y0,vy0,t,ay))
              t = t + delt    # increment time forward by delta t
       plt.plot(x, y)    # Plot the function
       plt.show()

inputs()    

init()  

plot_data()

