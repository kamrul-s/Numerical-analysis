import math

inpo=open('in2.txt','r').readlines()
eqnn=len(inpo)
spl=inpo[0].split(' ')
vn=(len(spl))
r,c=(eqnn,vn+1)
equ = [[0 for i in range(c)] for j in range(r)]
ansval= [0 for i in range(eqnn-1)]
for i in range(eqnn-1):
    ansval[i]=i+vn+1
anstem= [0 for i in range(eqnn-1+vn)]
for i in range(eqnn-1+vn):
    anstem[i]=i+1
for i in range(eqnn):
    equ[i]=inpo[i].split(' ')
    le=len(equ[i])
    for j in range(le):
        equ[i][j]=float(equ[i][j])

r,c=(eqnn,eqnn+vn+2)
mat = [[0 for i in range(c)] for j in range(r)] 
for i in range(r):
    for j in range(c):
        if i==0 and j==0:
            mat[i][j]=1
        elif i==0 and j<=vn:
            mat[0][j]=equ[0][j-1]*-1
        elif i==0:
            mat[i][j]=0
        else :
            if j==0:
                mat[i][j]=0
            elif j<=vn:
                mat[i][j]=equ[i][j-1]
            elif j==vn+i:
                mat[i][j]=1
            elif j==c-2:
                mat[i][j]=equ[i][vn]
            else :
                mat[i][j]=0
print('In teh tablu the coloum are as given as:')
print('   Z',end="\t")
for i in range(1,vn+1):
    print('X',i,end="\t")
for i in range(1,eqnn):
    print('S',i,end="\t")
print('Solution',end='  ')
print('Intercept')
print()
for i in range(r):
    tempo=mat[i]
    tempo=[ '%.2f' % elem for elem in tempo ]
    print(tempo)
print()
while 1==1:
    sm=0
    sj=0
    for i in range(c-1):
        if mat[0][i]<sm:
            sm=mat[0][i]
            sj=i
    if sm==0:
        break
    for i in range(1,r):
        if mat[i][sj]==0:
            mat[i][c-1]=math.inf
        else :
            mat[i][c-1]=mat[i][c-2]/mat[i][sj]
    for i in range(r):
        tempo=mat[i]
        tempo=[ '%.2f' % elem for elem in tempo ]
        print(tempo)
    print()
    smm=math.inf
    sjj=1
    for i in range(1,r):
        if mat[i][c-1]<smm and mat[i][c-1]>=0:
            smm=mat[i][c-1]
            sjj=i
    for i in range(r):
        mat[i][c-1]=0
    xte=mat[sjj][sj]
    for i in range(1,c):
        mat[sjj][i]=mat[sjj][i]/xte
    for i in range(r):
        if not i==sjj:
            x=mat[i][sj]
            for j in range(1,c):
                mat[i][j]=mat[i][j]-(mat[sjj][j]*x)
    print('Next Tablu:')
    for i in range(r):
        tempo=mat[i]
        tempo=[ '%.2f' % elem for elem in tempo ]
        print(tempo)
    print()
    ansval[sjj-1]=anstem[sj-1]
Xans=[0 for i in range(vn)]
for i in range(eqnn-1):
    if ansval[i]<=vn:
        Xans[ansval[i]-1]=mat[i+1][c-2]
mat[0][c-2]="%.2f" % round(mat[0][c-2],4)
tempo=Xans
tempo=[ '%.2f' % elem for elem in tempo ]
print('The maximum value of object func is:',mat[0][c-2])
print('The value of corousponding X1,...Xn=',tempo)
