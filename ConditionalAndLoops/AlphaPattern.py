n=int(input())
i=1
p=65
while i<=n:
    j=1
    next_char=chr(p)
    while j<=i:
        print(chr(ord(next_char)),end='')
        j=j+1
    p=p+1
    print()
    i=i+1