def subarray(li,num):
    sum=0
    n=len(li)
    p1=0
    li2=[]
    p2=0
    while p2<n:
        while sum<=num and p2<n:
            sum=sum+li[p2]
            li2.append(li[p2])
            p2=p2+1
        while sum>sum and p1<n:
            sum=sum-li[p1]
            li2.pop(p1)
            p1=p1+1
    print(li2)
                
            

n=int(input())
li=[int(x) for x in input().split()]
num=int(input())
subarray(li,num)