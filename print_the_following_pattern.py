n=int(input())
m=1
for i in range(0,n):
    for j in range(n-1,i,-1):
        print(' ',end='')
    for j in range(0,m):
        print(m-i,end='')
    m+=2
    print('')