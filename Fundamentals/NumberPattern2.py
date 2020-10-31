n=int(input())
i=1
while i<=n:
    s=1
    while s<=(2*n)-(2*i):
        print(' ',end='')
        s=s+1
    j=1
    p=i
    while j<=i:
        print(p,end='')
        p=p+1
        j=j+1
    print()
    i=i+1
    