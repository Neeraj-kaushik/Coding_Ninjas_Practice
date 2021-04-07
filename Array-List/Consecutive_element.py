def is_consecutive(li):
    length=len(li)
    for i in range(length-1):
        for j in range(i+1,length):
            if li[i]>li[j]:
                li[i],li[j]=li[j],li[i]
    if length==1:
        return True
    for i in range(length-1):
        if li[i+1]-li[i]==1:
            return True
        else:
            return False
            break



t=int(input())
while t>0:
    n=int(input())
    li=[int(x) for x in input().split()]
    ans=is_consecutive(li)
    if ans:
        print('True')
    else:
        print('False')
    t=t-1