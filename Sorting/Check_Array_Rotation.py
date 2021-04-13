def check_ro(li):
    if li[0]-li[-1]>=1:
        for i in range(len(li)):
            for j in range(i+1,len(li)):
                if li[i]>li[j]:
                    num=j
                    break
        print(num)            
    else:
        print('0')

t=int(input())
while t>0:
    n=int(input())
    li=[int(x) for x in input().split()]
    check_ro(li)
    t=t-1
