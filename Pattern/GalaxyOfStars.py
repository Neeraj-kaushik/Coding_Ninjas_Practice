"""here the pattern is
   *
   **
   ***
   ****
   ***
   **
   *     """

n=int(input())
n1=(n+1)/2
n2=n//2
i=1
while i<=n1:
    j=1
    while j<=i:
        print('*',end='')
        j=j+1
    print()
    i=i+1
i=1
p=n2
while i<=n2:
    j=1
    while j<=p:
        print('*',end='')
        j=j+1
    p=p-1
    print()
    i=i+1