def rotate_array(li,a):
    li1=[]
    num=-1
    for i in range(len(li)):
        if li[i]==a:
            num=i
    for i in range(num+1,len(li)):
        li1.append(li[i])
    for i in range(0,num+1):
        li1.append(li[i])
    print(li1)


t=int(input())
while t>0:
    n=int(input())
    li=[int(x) for x in input().split()]
    a=int(input())
    rotate_array(li,a)
    t=t-1
