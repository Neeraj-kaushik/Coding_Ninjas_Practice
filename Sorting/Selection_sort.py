def selection_sort(li):
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if li[j]<li[i]:
                li[i],li[j]=li[j],li[i]
    print(li)

n=int(input())
li=[int(x) for x in input().split()]
selection_sort(li)