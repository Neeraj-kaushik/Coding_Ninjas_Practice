def alternative(li):
    length=len(li)
    i=0
    while i<=length-1:
        for j in range(length//2):
            if i%2==0:
                li[i]=li[j]
        i=i+1
    print(li)


t=int(input())
while t>0:
    n=int(input())
    li=[int(x) for x in input().split()]
    alternative(li)
    t-=1