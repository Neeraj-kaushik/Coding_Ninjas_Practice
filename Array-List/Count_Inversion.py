def count_inversion(li):
    count=0
    length=len(li)
    for i in range(length-1):
        for j in range(i+1,length):
            if li[i]>li[j]:
                count=count+1
    print(count)

n=int(input())
li=[int(x) for x in input().split()]
count_inversion(li)