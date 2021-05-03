from matplotlib import pyplot as plt

def Trap(h,f0,f1):
    f=(f0+f1)/2
    return f*h
def Simp13(h,f0,f1,f2):
    f=f0+(4*f1)+f2
    f=f/3
    return f*h
def Simp38(h,f0,f1,f2,f3):
    f=f0+(f1*3)+(f2*3)+f3
    f=f*3/8
    return f*h
    
def solve(n,x,f):
    h=x[1]-x[0]
    k=1
    sum=0
    z = [0 for i in range(n)]
    tnum=0
    s13num=0
    s38num=0
    for i in range(2,n):
        hf=x[i]-x[i-1]
        dif=hf-h
        if dif<0:
            dif=dif*(-1)
        if dif<.0000001:
            k=k+1
        else:
            if k==1:
                sum=sum+Trap(h,f[i-2],f[i-1])
                z[tnum+s13num+s38num]=1
                tnum=tnum+1
            elif k==2:
                sum=sum+Simp13(h,f[i-3],f[i-2],f[i-1])
                z[tnum+s13num+s38num]=2
                s13num=s13num+1
            else:
                te=k%3
                if te==0:
                    te1=int(k/3)
                    te2=i-k-1
                    for j in range(te1):
                        sum=sum+Simp38(h,f[te2],f[te2+1],f[te2+2],f[te2+3])
                        te2=te2+3
                        z[tnum+s13num+s38num]=3
                        s38num=s38num+1
                elif te==1:
                    te1=int((k-4)/3)
                    te2=i-k-1
                    for j in range(2):
                        sum=sum+Simp13(h,f[te2],f[te2+1],f[te2+2])
                        te=te+2
                        z[tnum+s13num+s38num]=2
                        s13num=s13num+1
                    for j in range(te1):
                        sum=sum+Simp38(h,f[te2],f[te2+1],f[te2+2],f[te2+3])
                        te2=te2+3
                        z[tnum+s13num+s38num]=3
                        s38num=s38num+1
                else:
                    te1=int((k-2)/3)
                    te2=i-k-1
                    sum=sum+Simp13(h,f[te2],f[te2+1],f[te2+2])
                    te=te+2
                    z[tnum+s13num+s38num]=2
                    s13num=s13num+1
                    for j in range(te1):
                        sum=sum+Simp38(h,f[te2],f[te2+1],f[te2+2],f[te2+3])
                        te2=te2+3
                        z[tnum+s13num+s38num]=3
                        s38num=s38num+1
            h=hf
            k=1
    if k==1:
        sum=sum+Trap(h,f[i-2],f[i-1])
        z[tnum+s13num+s38num]=1
        tnum=tnum+1
    elif k==2:
        sum=sum+Simp13(h,f[i-3],f[i-2],f[i-1])
        z[tnum+s13num+s38num]=2
        s13num=s13num+1
    elif k>2:
        te=k%3
        if te==0:
            te1=int(k/3)
            te2=i-k-1
            for j in range(te1):
                sum=sum+Simp38(h,f[te2],f[te2+1],f[te2+2],f[te2+3])
                te2=te2+3
                z[tnum+s13num+s38num]=3
                s38num=s38num+1
        elif te==1:
            te1=int((k-4)/3)
            te2=i-k-1
            for j in range(2):
                sum=sum+Simp13(h,f[te2],f[te2+1],f[te2+2])
                te=te+2
                z[tnum+s13num+s38num]=2
                s13num=s13num+1
            for j in range(te1):
                sum=sum+Simp38(h,f[te2],f[te2+1],f[te2+2],f[te2+3])
                te2=te2+3
                z[tnum+s13num+s38num]=3
                s38num=s38num+1
        else:
            te1=int((k-2)/3)
            te2=i-k-1
            sum=sum+Simp13(h,f[te2],f[te2+1],f[te2+2])
            te=te+2
            z[tnum+s13num+s38num]=2
            s13num=s13num+1
            for j in range(te1):
                sum=sum+Simp38(h,f[te2],f[te2+1],f[te2+2],f[te2+3])
                te2=te2+3
                z[tnum+s13num+s38num]=3
                s38num=s38num+1
    return sum,tnum,s13num,s38num,z
           
inpo=open('input.txt','r').readlines()
n=int(inpo[0]) 
x = [0 for i in range(n)]
y = [0 for i in range(n)]
for i in range(n):
    spl=inpo[i+1].split(' ')
    x[i]=float(spl[0])
    y[i]=float(spl[1])


sum,tnum,s13num,s38num,z=solve(n,x,y)
print("Trapeziod: ",tnum," intervals")
print("1/3 rule: ",2*s13num," intervals")
print("3/8 rule: ",3*s38num," intervals")
print("Integral value: ",sum)

plt.scatter(x,y,s=15)
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.grid()
plt.plot(x,y,label='line',color='blue',linewidth=2)
plt.legend()
tx=[0 for i in range(2)]
ty=[0 for i in range(2)]
s13x=[0 for i in range(3)]
s13y=[0 for i in range(3)]
s38x=[0 for i in range(4)]
s38y=[0 for i in range(4)]
j=0
for i in range(tnum+s13num+s38num):
    if(z[i]==1):
        for k in range(2):
            tx[k]=x[j+k]
            ty[k]=0
        j=j+1
        plt.plot(tx,ty,color='red',linewidth=3)
    elif(z[i]==2):
        for k in range(3):
            s13x[k]=x[j+k]
            s13y[k]=0
        j=j+2
        plt.plot(s13x,s13y,color='black',linewidth=3)
    else :
        for k in range(4):
            s38x[k]=x[j+k]
            s38y[k]=0
        j=j+3
        plt.plot(s38x,s38y,color='yellow',linewidth=3)
plt.plot(tx,ty,label='Trapezoidal',color='red',linewidth=3)
plt.plot(s13x,s13y,label='1/3 rule',color='black',linewidth=3)
plt.plot(s38x,s38y,label='3/8 rule',color='yellow',linewidth=3)
az=[0 for i in range(n)]
plt.scatter(x,az,color='blue',s=15)    
plt.legend()     


  