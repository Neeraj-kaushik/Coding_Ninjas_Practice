def insertion_sort(li):
    length=len(li)
    for i in range(1,length):
        j=i-1
        temp=li[i]
        while j>=0 and li[j]>temp:
            li[j+1]=li[j]
            j=j-1
        li[j+1]=temp
    print(li)

t=int(input())
while t>0:
    n=int(input())
    li=[int(x) for x in input().split()]
    insertion_sort(li)