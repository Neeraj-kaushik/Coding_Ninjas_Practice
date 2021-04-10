def bubble_sort(li,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    print(li)

t=int(input())
while t>0:
    n=int(input())
    li=[int(x) for x in input().split()]
    bubble_sort(li,n)
    t=t-1
