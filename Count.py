n=int(input())
a=list(map(int,input().split()))
c=0
d=0
for i in range(n):
    if (a[i]%2==0):
        c+=1
    else:
        d+=1
print(c,d)