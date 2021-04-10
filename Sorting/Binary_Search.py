def binary_search(li,n,x):
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if x<li[mid]:
            end=mid-1
        elif x>li[mid]:
            start=mid+1
        else:
            return mid
    return -1

n=int(input())
li=[int(x) for x in input().split()]
t=int(input())
while t>0:
    x=int(input())
    print(binary_search(li,n,x))
    t=t-1
