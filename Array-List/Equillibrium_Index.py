def equillibrium_index(li):
    for i in range(len(li)):
        leftsum=0
        for j in range(i):
            leftsum=leftsum+li[j]
        rightsum=0
        for j in range(i+1,len(li)):
            rightsum=rightsum+li[j]
        if leftsum==rightsum:
            return i
    return -1
    
        

t=int(input())
while t>0:
    n=int(input())
    li=[int(x) for x in input().split()]
    print(equillibrium_index(li))
    t=t-1
