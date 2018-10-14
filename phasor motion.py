
from vpython import *

from math import *


xaxis=curve(vec(-5,0,0),vec(5,0,0))

yaxis=curve(vec(0,-5,0),vec(0,5,0))

a1=1
phi1=pi/3
phi2=pi/2


phasor1=arrow(pos=vec(0,0,0),axis=vec(1,1,0),color=color.green)

phasor2=arrow(axis=vec(a1*cos(phi2),a1*sin(phi2),0),pos=vec(0,0,0),color=color.red)
phasor_sum=arrow(pos=vec(0,0,0),axis=phasor1.axis+phasor2.axis,color=color.white)


omega1=2.0
omega2=3.0


dt=0.05

while True:
    rate(50)
    phasor1.axis=vec(a1*cos(phi1),a1*sin(phi1),0)
    phi1=phi1+omega1*dt
    phasor2.axis=vec(a1*cos(phi2),a1*sin(phi2),0)
    phi2=phi2+omega2*dt
    phasor_sum.axis=phasor1.axis+phasor2.axis

