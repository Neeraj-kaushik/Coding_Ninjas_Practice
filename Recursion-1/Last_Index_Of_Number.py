def findIndex(li, x):
    if len(li) == 0:
        return -1
    smalla = findIndex(li[1:], x)
    if smalla == -1:
        if li[0] == x:
            return 0
        else:
            return -1
    else:
        return smalla+1


li = [int(x) for x in input().split()]
x = int(input())
print(findIndex(li, x))
