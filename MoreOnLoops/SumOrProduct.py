"""Write a program that asks the user for a number N and a choice C. And then give them the possibility to choose between computing the sum and computing the product of all integers in the range 1 to N (both inclusive).
 """

n=int(input())
choice=int(input())
sum1=0
mul=1
if choice==1:
    for i in range(1,n+1):
        sum1=sum1+i
    print(sum1)
elif choice==2:
    for i in range(1,n+1):
        mul=mul*i
    print(mul)
else:
    print('-1')
