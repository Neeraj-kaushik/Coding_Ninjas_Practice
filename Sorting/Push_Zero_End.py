def push_0_end(li):
    num=0
    for i in range(len(li)):
        if li[i]!=0:
            temp=li[i]
            li[i]=li[num]
            li[num]=temp
            num=num+1
    print(li)

t=int(input())
while t>0:
    n=int(input())
    li=[int(x) for x in input().split()]
    push_0_end(li)
    t=t-1