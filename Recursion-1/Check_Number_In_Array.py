def checknum(li, x):
    if len(li) == 0:
        return False
    if li[0] == x:
        return True
    smallarr = checknum(li[1:], x)
    return smallarr


li = [int(x) for x in input().split()]
x = int(input())
if checknum(li, x):
    print('true')
else:
    print('false')
