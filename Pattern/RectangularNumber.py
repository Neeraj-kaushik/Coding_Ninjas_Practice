""" here the pattern is 
    4444444
    4333334
    4322234
    4321234
    4322234
    4333334  
    4444444   """

n=int(input())
for i in range (1,2*n,1):
    k=n
    if i<=n:
        for j in range (1,2*n,1):
            print(k,end="")
            if i>j:
                k=k-1
            if i+j>=2*n:
                k=k+1
    if i>n:
        for j in range (1,2*n,1):
            print(k,end="")
            if i+j<2*n:
                k=k-1
            if j>=i:
                k=k+1
    print()