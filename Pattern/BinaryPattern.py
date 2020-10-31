"""here the pattern is 
   1111
   000
   11
   0    """
   
n=int(input())
i=1
p=n
while i<=n:
    j=1
    while j<=p:
        if i%2==0:
            print('0',end='')
        else:
            print('1',end='')
        j=j+1
    p=p-1
    print()
    i=i+1

    