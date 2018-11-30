# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:38:49 2018

@author: Cole
"""

# Cole Grabowski
# Biocomputing Dynamic Modelling Project
# Dynamically model the rosenweig - MacArthur model of predator-prey relationships
# This model adds 2 terms to the Lotka- Volterra Model
#############################################
#
# Generate a script that uses a number of model simulations to demonstrate
# How each parameter affects the dynamics of the populations


# Import required packages
import scipy
import scipy.integrate as spint
import numpy
import pandas
from plotnine import *



def RMA_Sim(y,t0,b,alpha,w,d,e,s):
    H=y[0]
    P=y[1]
    
    dHdt=b*H*(1-alpha*H)-w*(H)/(d+H)*P # Herbivore governing equation
    dPdt=e*w*(H)/(d+H)*P-s*P  # Predator governing Equation
    
    return [dHdt,dPdt]

#######################
# case 1: Given values
times=numpy.arange(0,100,0.1) # passed to RMA_Sim as t0, step from 0 to 100 in increments of 0.1
y0=[500,120] # passed to RMA_Sim as y in this case, you can call it y0=y0 since y is just understood as the first argument given and called
 # y0 contains H_initial (starting herbivore population) and P_initial (starting predator population)

# b represents prey birth rate
b=0.8
 
# alpha represents 1/carrying capacity
alpha=0.001
 
# w represents search rate (units of area per time)
w=5
 
# d represents density of prey at which the predators kill rate reaches half its maximum
d=400

# e represents the conversion efficiency of prey to predators
e=0.07 

# s represents the predator death rate
s=0.2

params=(b,alpha,w,d,e,s) # params given in the order of LotVolSim function call above
sim=spint.odeint(func=RMA_Sim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a1=ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a1)



### For changing the parameters, go through each parameter and do one trial each at triple and half
### Do this for all parameters params=(b,alpha,w,d,e,s)


############### Change b (first by triple, then by 1/2)
######## Case 2: Triple b
params=(b*3,alpha,w,d,e,s) # params given in the order of LotVolSim function call above
sim=spint.odeint(func=RMA_Sim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a2=ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a2)

######## Case 3: Halve b
params=(b*0.5,alpha,w,d,e,s) # params given in the order of LotVolSim function call above
sim=spint.odeint(func=RMA_Sim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a3=ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a3)






############### Change alpha (first by triple, then by 1/2)
######## Case 4: Triple alpha
params=(b,alpha*3,w,d,e,s) # params given in the order of LotVolSim function call above
sim=spint.odeint(func=RMA_Sim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a4=ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a4)

######## Case 5: Halve alpha
params=(b,alpha*0.5,w,d,e,s) # params given in the order of LotVolSim function call above
sim=spint.odeint(func=RMA_Sim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a5=ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a5)



############### Change w (first by triple, then by 1/2)
######## Case 6: Triple w
params=(b,alpha,w*3,d,e,s) # params given in the order of LotVolSim function call above
sim=spint.odeint(func=RMA_Sim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a6=ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a6)

######## Case 7: Halve w
params=(b,alpha,w*0.5,d,e,s) # params given in the order of LotVolSim function call above
sim=spint.odeint(func=RMA_Sim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a7=ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a7)


############### Change d (first by triple, then by 1/2)
######## Case 8: Triple d
params=(b,alpha,w,d*3,e,s) # params given in the order of LotVolSim function call above
sim=spint.odeint(func=RMA_Sim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a8=ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a8)

######## Case 9: Halve d
params=(b,alpha,w,d*0.5,e,s) # params given in the order of LotVolSim function call above
sim=spint.odeint(func=RMA_Sim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a9=ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a9)


############### Change e (first by triple, then by 1/2)
######## Case 10: Triple e
params=(b,alpha,w,d,e*3,s) # params given in the order of LotVolSim function call above
sim=spint.odeint(func=RMA_Sim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a10=ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a10)

######## Case 11: Halve e
params=(b,alpha,w,d,e*0.5,s) # params given in the order of LotVolSim function call above
sim=spint.odeint(func=RMA_Sim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a11=ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a11)


############### Change s (first by triple, then by 1/2)
######## Case 12: Triple s
params=(b,alpha,w,d,e,s*3) # params given in the order of LotVolSim function call above
sim=spint.odeint(func=RMA_Sim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a12=ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a12)

######## Case 13: Halve s
params=(b,alpha,w,d,e,s*0.5) # params given in the order of LotVolSim function call above
sim=spint.odeint(func=RMA_Sim,y0=y0,t=times,args=params)
simDF=pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a13=ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a13)











