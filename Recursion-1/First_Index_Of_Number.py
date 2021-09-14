def index_of_number(li, x):
    if len(li) == 0:
        return -1
    if li[0] == x:
        return 0
    smalla = index_of_number(li[1:], x)
    if smalla == -1:
        return -1
    else:
        return smalla+1


li = [int(x) for x in input().split()]
x = int(input())
print(index_of_number(li, x))
