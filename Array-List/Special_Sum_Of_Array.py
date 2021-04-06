def array_sum(sum):
    new =0
    while sum!=0:
        rem=sum%10
        new=new+rem
        sum=sum//10
    return new

def special_sum(li):
    sum=0
    for i in range(len(li)):
        sum=sum+li[i]
    sum=array_sum(sum)
    if sum>=9:
        etc=array_sum(sum)
    print(etc)

n=int(input())
li=[int(x) for x in input().split()]
special_sum(li)