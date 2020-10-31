"""here the pattern is 
   1
   3 2
   4 5 6
   10 9 8 7
   11 12 13 14 15    """



n=int(input())
i=1
p=0
while i<=n:
    if i%2==0:
        j=1
        k=p+i
        p=k
        while j<=i:
            print(k,' ',end='')
            k=k-1
            j=j+1
    else:
        j=1
        while j<=i:
            p=p+1
            print(p,' ',end='')
            j=j+1
    print()
    i=i+1
