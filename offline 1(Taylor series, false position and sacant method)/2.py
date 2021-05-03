import numpy as np
from matplotlib import pyplot as plt
def f1(x):
    p=x/(1-x)
    q=p
    q=6/(2+x)
    q=np.sqrt(q)
    return (p*q)-0.05

def false_pos(xl,xu,es,maxi):
    if not (f1(xl)*f1(xu)<0) :
        print('Please give correct input')
        return -1
    i=0
    ea=1+es
    xro=0
    while ea>es and i<maxi:
        tem1=f1(xu)
        tem2=f1(xl)
        tem3=tem1*(xl-xu)/(tem2-tem1)
        xr=xu-tem3
        i=i+1
        if not (i==1 or xr==0):
            ea=abs((xr-xro)/xr)*100
        test=f1(xl)*f1(xr)
        if test==0:
            ea=0
        elif test<0:
            xu=xr
            xro=xr
        else :
            xl=xr
            xro=xr
    print('solution is',xr,'the value of fun at that point',f1(xr),'aprox rel. error',ea,'iteration num.',i)
    return 1

def secant(x1,x2,es,maxi):
    if not (f1(xl)*f1(xu)<0) :
        print('Please give correct input')
        return -1
    i=0
    while i<maxi:
        i=i+1
        xo=(x1*f1(x2)-x2*f1(x1))/(f1(x2)-f1(x1))
        c = f1(x1) * f1(xo)
        x1 = x2
        x2 = xo
        if c==0:
            break
        xm = (x1 * f1(x2) - x2 * f1(x1)) / (f1(x2) - f1(x1))
        if abs(xm - xo) < es:
            break
    print('solution is',xo,'iteration num.',i)
    return 1

        

#for ques 1
y=np.arange(-1,1,.1)
z=f1(y)
plt.plot(y,z,label='Built in ln(1+x)',color='red',linewidth=1)
plt.legend()
plt.grid()
plt.xlabel('X Label')
plt.ylabel('f(x) label')
plt.title('To solve a equation')
#so from the graph we can see that the value is nearer 0
print('so from the graph we can see that the value is nearer 0')

#for ques 2
while 1:
    #xu=eval(input('Enter the value of xu:'))
    #xl=eval(input('Enter the value of xu:'))
    xl=.9
    xu=0
    a=false_pos(xl,xu,.5,200)
    if a==1:
        break

#for ques 3
while 1:
    #x1=eval(input('Enter the value of xu:'))
    #x2=eval(input('Enter the value of xu:'))
    x1=.9
    x2=0
    a=secant(x1,x2,.005,200)
    if a==1:
        break









