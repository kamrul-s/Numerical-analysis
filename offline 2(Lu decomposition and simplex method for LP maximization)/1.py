def LU_decompose(a,n):
    r,c=(n,n)
    L=[[0 for i in range(c)] for j in range(r)] 
    U=[[0 for i in range(c)] for j in range(r)] 
    for i in range(n):
        for j in range(n):
            L[i][j]=0
            U[i][j]=a[i][j]

    for i in range(n-1):
        for j in range(i+1,n):
            x=U[j][i]/U[i][i]
            L[j][i]=x
            for k in range(n):
                U[j][k]=U[j][k]-(x*U[i][k])
    for i in range(n):
        L[i][i]=1
    return L,U

def gety(L,b,n):
    Y=[0 for i in range(n)]
    Y[0]=b[0]
    for i in range(1,n):
        sum=0
        for j in range(i):
            sum=sum+(L[i][j]*Y[j])
        Y[i]=b[i]-sum
    return Y
def getx(U,Y,n):
    X=[0 for i in range(n)]
    X[n-1]=Y[n-1]/U[n-1][n-1]
    for i in range(1,n):
        te=n-i-1
        sum=0
        for j in range(i):
            sum=sum+(U[te][n-1-j]*X[n-1-j])        
        X[te]=Y[te]-sum
        X[te]=X[te]/U[te][te]
    return X


#input
inpo=open('in1.txt','r').readlines()
n=int(inpo[0])
r,c=(n,n)
a = [[0 for i in range(c)] for j in range(r)] 
r,c=(n,1)
b=[[0 for i in range(c)] for j in range(r)] 
for i in range(n):
    spl=inpo[i+1].split(' ')
    for j in range(n):
        a[i][j]=float(spl[j])
for i in range(n):
    b[i]=float(inpo[i+n+1][0])

#calculate 
L,U=LU_decompose(a,n)
k=0
for i in range(n):
    temp=0
    for j in range(n):
        if U[i][j]==0:
            temp=temp+1
    if temp==n :
        k=1
        break
if k==0:
    Y=gety(L,b,n)
    X=getx(U,Y,n)
tem2=L
#l to file
out=open('out1.txt','w+')
for i in range(n):
    for j in range(n-1):
        tem2[i][j]="%.4f" % round(tem2[i][j],4)
        out.write(str(tem2[i][j]))
        out.write(' ')
    tem2[i][n-1]="%.4f" % round(tem2[i][n-1],4)
    out.write(str(tem2[i][n-1]))
    out.write('\n')
out.write('\n')
#u to file
tem3=U
for i in range(n):
    for j in range(n-1):
        tem3[i][j]="%.4f" % round(tem3[i][j],4)
        out.write(str(tem3[i][j]))
        out.write(' ')
    tem3[i][n-1]="%.4f" % round(tem3[i][n-1],4)
    out.write(str(tem3[i][n-1]))
    out.write('\n')
out.write('\n')
#not going forward
if k==1:
    out.write('No unique solution')
#Y to file
else:
    tem4=Y
    tem5=X
    for i in range(n):
        tem4[i]="%.4f" % round(tem4[i],4)
        out.write(str(tem4[i]))
        out.write('\n')
    out.write('\n')
    for i in range(n):
        tem5[i]="%.4f" % round(tem5[i],4)
        out.write(str(tem5[i]))
        out.write('\n')
    
out.close()