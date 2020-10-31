"""
Given a binary number as an integer N, convert it into decimal and print."""

n=int(input())
x=0
rev=0
while n!=0:
    rem=n%10
    rev=rev+pow(2,x)*rem
    x=x+1
    n=n//10
print(rev)