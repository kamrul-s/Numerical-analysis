from math import sin
from matplotlib import pyplot as plt
def fun(x,y):
    temp=(x+(20*y))
    temp2=sin(x*y)
    return temp*temp2
def Eular(stp):
    l=10/stp
    l=int(l)
    l=l+1
    x=[0 for i in range(l)]
    y=[0 for i in range(l)]
    print('x=0 y=4')
    x[0]=0
    y[0]=4
    i=1
    while True:
        tem=fun(x[i-1],y[i-1])
        y[i]=y[i-1]+tem*stp
        x[i]=x[i-1]+stp
        print('x=',round(x[i],3),'y=',y[i])
        if round(x[i],3)>=10:
            break
        i=i+1
    return x,y
def Heun(stp):
    l=10/stp
    l=int(l)
    l=l+1
    x=[0 for i in range(l)]
    y=[0 for i in range(l)]
    print('x=0 y=4')
    x[0]=0
    y[0]=4
    i=1
    while True:
        tem=fun(x[i-1],y[i-1])
        tem2=y[i-1]+tem*stp
        x[i]=x[i-1]+stp
        tem3=(fun(x[i-1],y[i-1])+fun(x[i],tem2))/2
        y[i]=y[i-1]+tem3*stp
        print('x=',round(x[i],3),'y=',y[i])
        if round(x[i],3)>=10:
            break
        i=i+1
    return x,y
def Midpoint(stp):
    l=10/stp
    l=int(l)
    l=l+1
    x=[0 for i in range(l)]
    y=[0 for i in range(l)]
    print('x=0 y=4')
    x[0]=0
    y[0]=4
    i=1
    while True:
        tem=fun(x[i-1],y[i-1])
        tem2=y[i-1]+(tem*stp/2)
        x[i]=x[i-1]+stp
        tem3=fun(x[i-1]+(stp/2),tem2)
        y[i]=y[i-1]+tem3*stp
        print('x=',round(x[i],3),'y=',y[i])
        if round(x[i],3)>=10:
            break
        i=i+1
    return x,y
def Ralston(stp):
    l=10/stp
    l=int(l)
    l=l+1
    x=[0 for i in range(l)]
    y=[0 for i in range(l)]
    print('x=0 y=4')
    x[0]=0
    y[0]=4
    i=1
    while True:
        tem=fun(x[i-1],y[i-1])
        x[i]=x[i-1]+stp
        tem2=fun(x[i-1]+(3*stp/4),y[i-1]+(3*tem*stp/4))
        y[i]=y[i-1]+(((tem/3)+(2*tem2/3))*stp)
        print('x=',round(x[i],3),'y=',y[i])
        if round(x[i],3)>=10:
            break
        i=i+1
    return x,y
def rk2(stp,a2):
    if abs(a2-1)<.001:
        return Midpoint(stp)
    elif  abs(a2-.5)<.001:
        return Heun(stp)
    elif abs(a2-(2/3))<.001:
        return Ralston(stp)
        
def rk4(stp):
    l=10/stp
    l=int(l)
    l=l+1
    x=[0 for i in range(l)]
    y=[0 for i in range(l)]
    print('x=0 y=4')
    x[0]=0
    y[0]=4
    i=1
    while True:
        k1=fun(x[i-1],y[i-1])
        k2=fun(x[i-1]+(stp/2),y[i-1]+(k1*stp/2))
        k3=fun(x[i-1]+(stp/2),y[i-1]+(k2*stp/2))
        k4=fun(x[i-1]+stp,y[i-1]+(k3*stp))
        y[i]=y[i-1]+((k1+(2*k2)+(2*k3)+k4)*stp/6)
        x[i]=x[i-1]+stp
        print('x=',round(x[i],3),'y=',y[i])
        if round(x[i],3)>=10:
            break
        i=i+1
    return x,y

plt.figure(1)  
ex1,ey1=Eular(.01)
ex2,ey2=Eular(.05)
ex3,ey3=Eular(.1)
ex4,ey4=Eular(.5)
plt.plot(ex1,ey1,label='step .01',linewidth=2)
plt.plot(ex2,ey2,label='step .05',linewidth=2)
plt.plot(ex3,ey3,label='step .1',linewidth=2)
plt.plot(ex4,ey4,label='step .1',linewidth=2)
plt.legend()
plt.grid()
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('Eular')


plt.figure(2)  
ex1,ey1=Heun(.01)
ex2,ey2=Heun(.05)
ex3,ey3=Heun(.1)
ex4,ey4=Heun(.5)
plt.plot(ex1,ey1,label='step .01',linewidth=2)
plt.plot(ex2,ey2,label='step .05',linewidth=2)
plt.plot(ex3,ey3,label='step .1',linewidth=2)
plt.plot(ex4,ey4,label='step .1',linewidth=2)
plt.legend()
plt.grid()
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('Heun')

plt.figure(3)  
ex1,ey1=Midpoint(.01)
ex2,ey2=Midpoint(.05)
ex3,ey3=Midpoint(.1)
ex4,ey4=Midpoint(.5)
plt.plot(ex1,ey1,label='step .01',linewidth=2)
plt.plot(ex2,ey2,label='step .05',linewidth=2)
plt.plot(ex3,ey3,label='step .1',linewidth=2)
plt.plot(ex4,ey4,label='step .1',linewidth=2)
plt.legend()
plt.grid()
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('Midpoint')

plt.figure(4)  
ex1,ey1=Ralston(.01)
ex2,ey2=Ralston(.05)
ex3,ey3=Ralston(.1)
ex4,ey4=Ralston(.5)
plt.plot(ex1,ey1,label='step .01',linewidth=2)
plt.plot(ex2,ey2,label='step .05',linewidth=2)
plt.plot(ex3,ey3,label='step .1',linewidth=2)
plt.plot(ex4,ey4,label='step .1',linewidth=2)
plt.legend()
plt.grid()
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('Ralston')

plt.figure(5)  
ex1,ey1=rk4(.01)
ex2,ey2=rk4(.05)
ex3,ey3=rk4(.1)
ex4,ey4=rk4(.5)
plt.plot(ex1,ey1,label='step .01',linewidth=3)
plt.plot(ex2,ey2,label='step .05',linewidth=3)
plt.plot(ex3,ey3,label='step .1',linewidth=3)
plt.plot(ex4,ey4,label='step .1',linewidth=3)
plt.legend()
plt.grid()
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('Rk4')

plt.figure(6)  
ex1,ey1=Eular(.01)
ex2,ey2=Heun(.01)
ex3,ey3=Midpoint(.01)
ex4,ey4=Ralston(.01)
ex5,ey5=rk4(.01)
plt.plot(ex1,ey1,label='eular',linewidth=2)
plt.plot(ex2,ey2,label='Heun',linewidth=2)
plt.plot(ex3,ey3,label='Midpoint',linewidth=2)
plt.plot(ex4,ey4,label='Ralston',linewidth=2)
plt.plot(ex5,ey5,label='rk4',linewidth=2)
plt.legend()
plt.grid()
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('Step .01')

plt.figure(7)  
ex1,ey1=Eular(.05)
ex2,ey2=Heun(.05)
ex3,ey3=Midpoint(.05)
ex4,ey4=Ralston(.05)
ex5,ey5=rk4(.05)
plt.plot(ex1,ey1,label='eular',linewidth=2)
plt.plot(ex2,ey2,label='Heun',linewidth=2)
plt.plot(ex3,ey3,label='Midpoint',linewidth=2)
plt.plot(ex4,ey4,label='Ralston',linewidth=2)
plt.plot(ex5,ey5,label='rk4',linewidth=2)
plt.legend()
plt.grid()
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('Step .05')

plt.figure(8)  
ex1,ey1=Eular(.1)
ex2,ey2=Heun(.1)
ex3,ey3=Midpoint(.1)
ex4,ey4=Ralston(.1)
ex5,ey5=rk4(.1)
plt.plot(ex1,ey1,label='eular',linewidth=2)
plt.plot(ex2,ey2,label='Heun',linewidth=2)
plt.plot(ex3,ey3,label='Midpoint',linewidth=2)
plt.plot(ex4,ey4,label='Ralston',linewidth=2)
plt.plot(ex5,ey5,label='rk4',linewidth=2)
plt.legend()
plt.grid()
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('Step .1')

plt.figure(9)  
ex1,ey1=Eular(.5)
ex2,ey2=Heun(.5)
ex3,ey3=Midpoint(.5)
ex4,ey4=Ralston(.5)
ex5,ey5=rk4(.5)
plt.plot(ex1,ey1,label='eular',linewidth=2)
plt.plot(ex2,ey2,label='Heun',linewidth=2)
plt.plot(ex3,ey3,label='Midpoint',linewidth=2)
plt.plot(ex4,ey4,label='Ralston',linewidth=2)
plt.plot(ex5,ey5,label='rk4',linewidth=2)
plt.legend()
plt.grid()
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('Step .5')





