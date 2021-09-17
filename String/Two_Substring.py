str=input()
var1=str[0:len(str)//2]
var1=var1[::-1]
if var1 in str:
    print('NO')
else:
    print('YES')