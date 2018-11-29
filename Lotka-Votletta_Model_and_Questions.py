# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:03:05 2018

@author: Patrick
"""

#Lotka-Volterra Model describes two populations by two different equations

#Prey Population = H (Herbivore)
#Predator Population = P
#prey birth rate = b
#predator attack rate = a
#conversion efficiency of prey to predators = e
#predator death rate = s

#dH/dt = bH - aPH
#dP/dt = eaPH - sP

#Simulate dynamics with the following parameters and initial conditions
    #b=0.5, a=0.02, e=0.1, s-0.2, Ho=25, Po=5

#import necessary packages for running and plotting the simulations
import pandas as pd
from plotnine import *
import scipy.integrate as spint
import numpy as np

def LVSim(y,t0,b,a,e,s): #defining function to describe Lotka-Volterra model
    H=y[0] #sets the number that will define the herbivore population throughout the run time
    P=y[1] #sets number defining predator population during run time
    
    dHdt=b*H-a*P*H #equation to describe how prey population changes over time
    dPdt=e*a*P*H-s*P #equation to describe how predator population changes over time
    
    return [dHdt,dPdt] #returns your two variables (change in prey and change in predator)

times=np.arange(0,100,0.1) #defines length of the simulation - I chose 100 to see substantial ebbs and flows, time steps of 0.1 as recommended
y0=[25,5] #defining intial populations of prey (25) and preaotor (5) - these are initial y[0] and y[1] in the function above
params=(0.5,0.02,0.1,0.2) #defining the parameters for the LV plot - b, a, e, and s
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params) #runs the simulation for the time given (100) using LVplot as our defined function to run it
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]}) #Takes simulation results and puts them in a dataframe using pandas
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic() #plots the results for prey and predator populations over time from the dataframe created in the previous step

#In all cases, the predator population is defined by the red line and the prey population is defined by the red line

#Run a number of additional simulations changing one of the parameters at a time
#to learn how each parameters affects the dynamics of the populations
#(Should be able to increase/decrease each parameter as much as a factor of
#2 to 4 without causing major problems in the output)

#Triple the prey birth rate
times=np.arange(0,100,0.1)
y0=[25,5]
params=(1.5,0.02,0.1,0.2)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

#Reduce the prey birth rate from 0.5 to 0.2
times=np.arange(0,100,0.1)
y0=[25,5]
params=(0.2,0.02,0.1,0.2)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()
 
#Triple the predator attack rate
times=np.arange(0,100,0.1)
y0=[25,5]
params=(0.5,0.06,0.1,0.2)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

#Hlave the predator attack rate
times=np.arange(0,100,0.1)
y0=[25,5]
params=(0.5,0.01,0.1,0.2)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

#Triple the conversion efficiency of prey to preators
times=np.arange(0,100,0.1)
y0=[25,5]
params=(0.5,0.02,0.3,0.2)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

#Halve the conversion efficiency of prey to preators
times=np.arange(0,100,0.1)
y0=[25,5]
params=(0.5,0.02,0.05,0.2)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

#Triple the predator death rate
times=np.arange(0,100,0.1)
y0=[25,5]
params=(0.5,0.02,0.1,0.6)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

#Halve the predator death rate
times=np.arange(0,100,0.1)
y0=[25,5]
params=(0.5,0.02,0.1,0.1)
sim=spint.odeint(func=LVSim,y0=y0,t=times,args=params)
simDF=pd.DataFrame({"t":times,"prey":sim[:,0],"predator":sim[:,1]})
ggplot(simDF,aes(x="t",y="prey"))+geom_line()+geom_line(simDF,aes(x="t",y="predator"),color='red')+theme_classic()

