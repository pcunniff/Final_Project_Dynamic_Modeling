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

import pandas as pd
from plotnine import *
import scipy.integrate as spint

def LVSim(y,t0,b,a,e,s):
    H=y[0]
    P=y[1]
    
    dHdt=b*H-a*P*H
    dPdt=e*a*P*H-s*P
    
    return [dHdt,dPdt]

times=range(0,100)
y0=[25,5]
params=(0.5,0.02,0.1,0.2)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

#Run a number of additional simulations changing one of the parameters at a time
#to learn how each parameters affects the dynamics of the populations
#(Should be able to increase/decrease each parameter as much as a factor of
#2 to 4 without causing major problems in the output)

#Triple the prey birth rate
times=range(0,100)
y0=[25,5]
params=(1.5,0.02,0.1,0.2)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

#Reduce the prey birth rate from 0.5 to 0.2
times=range(0,100)
y0=[25,5]
params=(0.2,0.02,0.1,0.2)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()
 
#Triple the predator attack rate
times=range(0,100)
y0=[25,5]
params=(0.5,0.06,0.1,0.2)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

#Hlave the predator attack rate
times=range(0,100)
y0=[25,5]
params=(0.5,0.01,0.1,0.2)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

#Triple the conversion efficiency of prey to preators
times=range(0,100)
y0=[25,5]
params=(0.5,0.02,0.3,0.2)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

#Halve the conversion efficiency of prey to preators
times=range(0,100)
y0=[25,5]
params=(0.5,0.02,0.05,0.2)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

#Triple the predator death rate
times=range(0,100)
y0=[25,5]
params=(0.5,0.02,0.1,0.6)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

#Halve the predator death rate
times=range(0,100)
y0=[25,5]
params=(0.5,0.02,0.1,0.1)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

#What can you say about the "role" of each parameter


#What can you say about the rile of predators in the simuluations


#What is the relationship between parameter values and predator-prey cycle length

