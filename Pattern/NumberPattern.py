"""here the pattenr is 
   333
   233
   123  """

n=int(input())
i=1
p=n
while i<=n:
    j=1
    h=n
    k=h-i+1
    while j<=i-1:
        print(k,end='')
        k=k+1
        j=j+1
    j=1
    h=n
    while j<=p:

        print(h,end='')
        j=j+1
    p=p-1
    print()
    i=i+1