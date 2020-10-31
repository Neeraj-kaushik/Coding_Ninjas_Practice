n=int(input())
if n%2==0:
    n1=(n+2)/2
    n2=(n+1)/2
else:
    n1=(n+1)/2
    n2=n/2

i=1
while i<=n1:
    s=1 
    while s<=n1-i:
        print(' ',end='')
        s=s+1
    j=1
    k=(2*i)-1
    while j<=k:
        print(j,end='')
        j=j+1
    print()
    i=i+1
i=1
while i<=n2:
    s=1
    while s<=i:
        print(' ',end='')
        s=s+1
    j=1
    k=2*(n2-i)
    while j<=k:
        print(j,end='')
        j=j+1
    print()
    i=i+1