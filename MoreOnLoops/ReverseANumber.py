"""Write a program to generate the reverse of a given number N. Print the corresponding reverse number."""

def reverse(n):
    rev=0
    while n != 0:
        num=n%10
        rev=rev*10+num
        n=n//10
    return rev

n=int(input())
result = reverse(n)
print(result)