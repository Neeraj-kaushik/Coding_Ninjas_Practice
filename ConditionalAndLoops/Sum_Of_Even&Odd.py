num=int(input())
sum_of_even=0
sum_of_odd=0
while num !=0:
    num1=num%10
    if num1%2==0:
        sum_of_even=sum_of_even+num1
    else:
        sum_of_odd=sum_of_odd+num1
    num=num//10
print(sum_of_even," ",sum_of_odd)
