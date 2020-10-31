"""here the patterrn is 
   ABCCBA
    ABBA
     AA     """

n=int(input())
i=1
p=n
while i<=n:
    s=1
    while s<=i-1:
        print(' ',end='')
        s=s+1
    j=1
    nextchar=chr(ord('A'))
    while j<=p:
        newchar=chr(ord(nextchar)+j-1)
        print(newchar,end='')
        j=j+1
    j=p
    nextchar=chr(ord('A')+p-1)
    m=ord(nextchar)
    while j>=1:
        newchar=chr(m)
        print(newchar,end='')
        m=m-1
        j=j-1
    p=p-1
    print()
    i=i+1
