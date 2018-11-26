# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:03:05 2018

@author: Patrick
"""

#Lotka-Volterra Model describes two populations by two different equations

#Prey = H (Herbivore)
#Predator = P
#prey birth rate = b
#predator attack rate = a
#conversion efficiency of prey to predators = e
#predator death rate = s

#dH/dt = bH - aPH
#dP/dt = eaPH - sP

#Simulate dynamics with the following parameters and initial conditions
    #b=0.5, a=0.02, e=0.1, s-0.2, Ho=25, Po=5
    #simulations should be run with time steps of 0.1
from plotnine import *
from scipy.optimize import minimize
from scipy.stats import norm
import numpy as np
from scipy import stats



#Run a number of additional simulations changing one of the parameters at a time
#to learn how each parameters affects the dynamics of the populations
#(Should be able to increase/decrease each parameter as much as a factor of
#2 to 4 without causing major problems in the output)



#What can you say about the "role" of each parameter


#What can you say about the rile of predators in the simuluations


#What is the relationship between parameter values and predator-prey cycle length

