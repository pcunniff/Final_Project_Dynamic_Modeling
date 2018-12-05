import scipy
import scipy.integrate as spint
import numpy
import pandas
from plotnine import *

def RMA_Sim(y,t0,b,alpha,w,d,e,s):
    H=y[0]
    P=y[1]
    
    dHdt = b*H*(1-alpha*H)-w*(H)/(d+H)*P
    dPdt = e*w*(H)/(d+H)*P-s*P
    
    return [dHdt,dPdt]

times = numpy.arange(0,100,0.1) # passed to RMA_Sim as t0, step from 0 to 100 in increments of 0.1
y0=[500,120] # passed to RMA_Sim as y in this case, you can call it y0=y0 since y is just understood as the first argument given and called
# y0 contains H_initial (starting herbivore population) and P_initial (starting predator population)

# b represents prey birth rate
b = 0.8
# w represents search rate (units of area per time)
w = 5
# d represents density of prey at which the predators kill rate reaches half its maximum
d = 400
# e represents the conversion efficiency of prey to predators
e = 0.07 
# s represents the predator death rate
s = 0.2

# 1st simulation, carrying capacity = 800, alpha = 0.00125
params = (b, 0.00125, w, d, e, s) # params given in the order provided above, aside from the alpha value that varies every trial
sim = spint.odeint(func = RMA_Sim, y0 = y0, t = times, args = params)
simDF = pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a1 = ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a1)

# 2nd simulation, carrying capacity = 1200, alpha = 0.001
params = (b, 0.001, w, d, e, s)
sim = spint.odeint(func = RMA_Sim, y0 = y0, t = times, args = params)
simDF = pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a2 = ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a2)

# 3rd simulation, carrying capacity = 1600, alpha = 0.00075
params = (b, 0.00075, w, d, e, s)
sim = spint.odeint(func = RMA_Sim, y0 = y0, t = times, args = params)
simDF = pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a3 = ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a3)

# 4th simulation, carrying capacity = 2000, alpha = 0.0005
params = (b, 0.0005, w, d, e, s)
sim = spint.odeint(func = RMA_Sim, y0 = y0, t = times, args = params)
simDF = pandas.DataFrame({"Time":times,"Population":sim[:,0],"Population2":sim[:,1]})
a4 = ggplot(simDF,aes(x="Time",y="Population"))+geom_line()+geom_line(simDF,aes(x="Time",y="Population2"),color='red')+theme_classic()
print(a4)
