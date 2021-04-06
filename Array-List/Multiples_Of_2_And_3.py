def sum_of_multiple_of_2_and_3(li):
    sum=0
    for i in range(len(li)):
        if li[i]%2==0 or li[i]%3==0:
            sum=sum+li[i]
    print(sum)

n=int(input())
li=[int(x) for x in input().split()]
sum_of_multiple_of_2_and_3(li)