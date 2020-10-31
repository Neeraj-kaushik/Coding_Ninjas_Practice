"""Write a program to print first x terms of the series 3N + 2 which are not multiples of 4."""

n=int(input())
sum=0
i=1
m=1
while i<=n:
    sum=3*m+2
    m=m+1
    if sum%4!=0:
        print(sum,end=' ')
        i=i+1

