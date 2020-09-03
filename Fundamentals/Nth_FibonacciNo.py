num=int(input())
val1=0
val2=1
i=1
while i <num:
    fibo=val1+val2
    val1=val2
    val2=fibo
    i=i+1
print(fibo)