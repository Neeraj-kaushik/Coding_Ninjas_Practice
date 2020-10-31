"""here the pattern is 
   E
   DE
   CDE
   BCDE
   ABCDE   """
n=int(input())
i=1
p=n
while i<=n:
    j=1
    startchar=chr(ord('A')+p-1)
    while j<=i:
        newchar = chr(ord(startchar)+j-1)
        print(newchar,end='')
        j=j+1
    p=p-1
    print()
    i=i+1