def second_largest(li):
    li=sorted(li)
    length=len(li)
    if (length==2 or li[-1]==li[-2]) or (li[-2]<=1):
        print(-1)
    else:
        print(li[-2])
    

t=int(input())
while t>0:
    n=int(input())
    li=[int(x) for x in input().split()]
    second_largest(li)
    t=t-1
