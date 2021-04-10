def merge_sort(li1,n,li2,m):
    li3=[]
    i=0
    j=0
    while i<n and  j<m:
        if li1[i]<li2[j]:
            li3.append(li1[i])
            i=i+1
        else:
            li3.append(li2[j])
            j=j+1
    while i<n:
        li3.append(li1[i])
        i=i+1
    while j<m:
        li3.append(li2[j])
        j=j+1
    print(li3)

t=int(input())
while t>0:
    n=int(input())
    li1=[int(x) for x in input().split()]
    m=int(input())
    li2=[int(a) for a in input().split()]
    merge_sort(li1,n,li2,m)
    t=t-1