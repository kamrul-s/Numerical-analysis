import numpy as np
from matplotlib import pyplot as plt
import math

def f1(a0,a1,x):
    return (a0+(a1*x))
def f2(a0,a1,a2,x):
    return (a0+(a1*x)+(a2*x*x))
def f3(a0,a1,a2,a3,x):
    return (a0+(a1*x)+(a2*x*x)+(a3*x*x*x))


inpo=open('data.txt','r').readlines()
n=len(inpo)
x=[0 for i in range(n)]
y=[0 for i in range(n)]
for i in range(n):
    spl=inpo[i].split(' ')
    x[i]=float(spl[0])
    y[i]=float(spl[1])
plt.scatter(x,y,s=3)
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.legend()
plt.grid()
#deg 1
sumx=0
for i in range(n):
    sumx=sumx+x[i]

sumy=0
for i in range(n):
    sumy=sumy+y[i]
sumx2=0
for i in range(n):
    sumx2=sumx2+(x[i]*x[i])
sumy2=0
for i in range(n):
    sumy2=sumy2+(y[i]*y[i])
sumxy=0
for i in range(n):
    sumxy=sumxy+(x[i]*y[i])
a1=((n*sumxy)-(sumx*sumy))/((n*sumx2)-(sumx*sumx))
ybar=sumy/n
xbar=sumx/n
a0=ybar-(a1*xbar)
r=((n*sumxy)-(sumx*sumy))/(math.sqrt((n*sumx2)-(sumx*sumx))*math.sqrt((n*sumy2)-(sumy*sumy)))
print('for order 1')
print('a0=',a0)
print('a1=',a1)
print('r=',r)
#order 2
sumx3=0
for i in range(n):
    sumx3=sumx3+(x[i]*x[i]*x[i])
sumx4=0
for i in range(n):
    sumx4=sumx4+(x[i]*x[i]*x[i]*x[i])


meta= [[0 for i in range(3)] for j in range(3)] 
metb=[0 for i in range(3)]
for i in range(3):
    for j in range(3):
        if i==0 and j==0:
            meta[i][j]=n
        else :
            k=i+j
            if k==1:
                meta[i][j]=sumx
            elif k==2:
                meta[i][j]=sumx2
            elif k==3:
                meta[i][j]=sumx3
            elif k==4:
                meta[i][j]=sumx4
sumx2y=0
for i in range(n):
    sumx2y=sumx2y+(x[i]*x[i]*y[i])
metb[0]=sumy
metb[1]=sumxy
metb[2]=sumx2y
#print(meta)
aord2=np.linalg.solve(meta,metb)
st=0
sr=0
for i in range (n):
    sr=sr+((y[i]-f2(aord2[0],aord2[1],aord2[2],x[i]))*(y[i]-f2(aord2[0],aord2[1],aord2[2],x[i])))
ybar=sumy/n
for i in range(n):
    st=st+((ybar-y[i])*(ybar-y[i]))
r=math.sqrt((st-sr)/st)
print('For order 2')
print('a0=',aord2[0])
print('a1=',aord2[1])
print('a2=',aord2[2])
print('r=',r)

#deg3
meta1= [[0 for i in range(4)] for j in range(4)] 
metb1=[0 for i in range(4)]
sumx5=0
for i in range(n):
    sumx5=sumx5+(x[i]*x[i]*x[i]*x[i]*x[i])
sumx6=0
for i in range(n):
    sumx6=sumx6+(x[i]*x[i]*x[i]*x[i]*x[i]*x[i])

for i in range(4):
    for j in range(4):
        if i==0 and j==0:
            meta1[i][j]=n
        else :
            k=i+j
            if k==1:
                meta1[i][j]=sumx
            elif k==2:
                meta1[i][j]=sumx2
            elif k==3:
                meta1[i][j]=sumx3
            elif k==4:
                meta1[i][j]=sumx4
            elif k==5:
                meta1[i][j]=sumx5
            elif k==6:
                meta1[i][j]=sumx6
sumx3y=0
for i in range(n):
    sumx3y=sumx3y+(x[i]*x[i]*x[i]*y[i])
metb1[0]=sumy
metb1[1]=sumxy
metb1[2]=sumx2y
metb1[3]=sumx3y
aord3=np.linalg.solve(meta1,metb1)
#print(meta1)
st=0
sr=0
for i in range (n):
    sr=sr+((y[i]-f3(aord3[0],aord3[1],aord3[2],aord3[3],x[i]))*(y[i]-f3(aord2[0],aord2[1],aord2[2],aord3[3],x[i])))
ybar=sumy/n
for i in range(n):
    st=st+((ybar-y[i])*(ybar-y[i]))
r=math.sqrt((st-sr)/st)
print('For order 3')
print('a0=',aord3[0])
print('a1=',aord3[1])
print('a2=',aord3[2])
print('a3=',aord3[3])
print('r=',r)
z1=x
for i in range(n):
    for j in range(i+1,n):
        if z1[j]<z1[i]:
            t=z1[i]
            z1[i]=z1[j]
            z1[j]=t
z2=[0 for i in range(n)]
for i in range(n):
    z2[i]=f1(a0,a1,z1[i])
plt.plot(z1,z2,label='order 1 curve',color='red',linewidth=3)
plt.legend()
plt.grid()

z3=[0 for i in range(n)]
for i in range(n):
    z3[i]=f2(aord2[0],aord2[1],aord2[2],z1[i])
plt.plot(z1,z3,label='order 2 curve',color='black',linewidth=3)
plt.legend()
plt.grid()

z4=[0 for i in range(n)]
for i in range(n):
    z4[i]=f3(aord3[0],aord3[1],aord3[2],aord3[3],z1[i])
plt.plot(z1,z4,label='order 3 curve',color='purple',linewidth=3)
plt.legend()
plt.grid(True)
plt.title('this is graph of different order curve')













