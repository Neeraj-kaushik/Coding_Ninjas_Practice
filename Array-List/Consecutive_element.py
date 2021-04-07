def is_consecutive(li):
    length=len(li)
    for i in range(length-1):
        for j in range(i+1,length):
            if li[i]>li[j]:
                li[i],li[j]=li[j],li[i]
    if li[-1]-li[0]==length-1:
        return True
    else:
        return False



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