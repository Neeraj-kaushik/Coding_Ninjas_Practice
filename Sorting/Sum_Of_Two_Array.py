def sum_of_array(li,n,li1,m):
    


t=int(input())
while t>0:
    n=int(input())
    li=[int(x) for x in input().split()]
    m=int(input())
    li1=[int(a) for a in input().split()]
    sum_of_array(li,n,li1,m)
    t=t-1