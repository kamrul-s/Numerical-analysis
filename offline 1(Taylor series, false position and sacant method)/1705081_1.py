import numpy as np
from matplotlib import pyplot as plt
from math import log

def user_ln(x,n): #return ln(1+x)
    ans=0
    temp=x
    sign=1
    a=n
    n=n+1
    for i in range(a):
        i=i+1
        ans=ans+(sign*x/i)
        sign=sign*-1
        x=x*temp
    return ans

def rel_er(a,t):
    x=abs(a-t)
    x=x*100/t
    return x

#for ques 1
x=eval(input('Enter the value of x:'))
n=eval(input('Enter the iteration number:'))
print('the value of log(1+x) is',user_ln(x,n))

#for ques 2
plt.figure(1)  
x=np.arange(-1,1,.1)
y=np.log(1+x)
plt.plot(x,y,label='Built in ln(1+x)',color='black',linewidth=3)
plt.legend()
plt.grid()
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('this is built in ln(1+x)')

#for ques 3
plt.figure(2)  
x=np.arange(-1,1,.1)
y=np.log(1+x)
y1=user_ln(x,1)
y2=user_ln(x,3)
y3=user_ln(x,5)
y4=user_ln(x,20)
y5=user_ln(x,50)

plt.plot(x,y,label='Built in ln(1+x)',color='black',linewidth=5)
plt.plot(x,y1,label='ln(1+x) with term 1',linewidth=3)
plt.plot(x,y2,label='ln(1+x) with term 3',linewidth=3)
plt.plot(x,y3,label='ln(1+x) with term 5',linewidth=3)
plt.plot(x,y4,label='ln(1+x) with term 20',linewidth=3)
plt.plot(x,y5,label='ln(1+x) with term 50',linewidth=3)

plt.legend()
plt.grid()
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('this is ln(1+x)')

#for ques 4
plt.figure(3)  
tr=log(1.5)
y=np.arange(1,50,1)
z=[]
tr=log(1.5)
for j in range(1,50):
    z.append(rel_er(user_ln(.5,j),tr))
    
plt.plot(y,z,label='Relative error',linewidth=3)

plt.legend()
plt.grid()
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.title('Relative error')
    
    
    
    
    
    
    
    
    
    
    
    
    