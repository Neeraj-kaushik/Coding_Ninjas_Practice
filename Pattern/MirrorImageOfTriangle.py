"""here the pattern is
     0
    101
   21012  """

n=int(input())
i=1
g=n+1
while i<=g:
    s=1
    while s<=g-i:
        print(' ',end='')
        s=s+1
    j=0
    p=i
    while j<=i-1:
        print(p-1,end='')
        j=j+1
        p=p-1
    j=1
    p=i-1
    while p>=1:
        print(j,end='')
        j=j+1
        p=p-1
    print()
    i=i+1
