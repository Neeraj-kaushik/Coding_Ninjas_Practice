"""here the pattern is 
   ****
    ***
     **
      *    """

n=int(input())
i=1
p=n
while i<=n:
    s=1
    while s<=i-1:
        print(' ',end='')
        s=s+1
    j=1
    while j<=p:
        print('*',end='')
        j=j+1
    p=p-1
    print()
    i=i+1