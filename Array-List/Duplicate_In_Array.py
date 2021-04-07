def find_duplicate(li):
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if li[i]==li[j]:
                return li[i]
        

t= int(input())
while t>0:
    n=int(input())
    li=[int(x) for x in input().split()]
    li=find_duplicate(li)
    print(li)
    t=t-1