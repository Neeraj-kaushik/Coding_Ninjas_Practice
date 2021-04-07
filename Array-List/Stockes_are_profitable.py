def stockes(li):
    b=max(li)
    li1=[]
    for i in range(len(li)):
        if li[i] != b:
            li1.append(li[i])
        else:
            break
    a=min(li1)
    c=b-a
    print(c)
    



n=int(input())
li=[int(x) for x in input().split()]
stockes(li)