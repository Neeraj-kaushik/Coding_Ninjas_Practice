def checkMember(n):
    val1=0
    val2=1
    if n==val1 or n==val2:
        return True
    fab=val1+val2
    while fab<=n:
        if fab==n:
            return True
        val1=val2
        val2=fab
        fab=val1+val2
    return False


n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")