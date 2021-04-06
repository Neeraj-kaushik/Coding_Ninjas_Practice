def division_of_4(li):
    for i in range(len(li)):
        if li[i]//4==0:
            li[i]=-1
        else:
            li[i]=li[i]//4
    print(*li,sep=' ')

n=int(input())
li=[int(x) for x in input().split()]
division_of_4(li)