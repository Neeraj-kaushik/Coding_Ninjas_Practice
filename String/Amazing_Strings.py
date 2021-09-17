ascii=256
def amazing_string(str,str1,str2):
    count=[0]*ascii
    count1=[0]*ascii
    a=len(str)+len(str1)
    b=len(str2)
    if a==b:
        for i in str:
            count[ord(i)]+=1
        for i in str1:
            count1[ord(i)]+=1
        for j in str2:
            count2[ord(i)]+=1
        if count2[ord(j)]==count[ord(i)] and count2[ord(j)]==count1[ord(i)]:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')


str=intput()
str1=input()
str2=input()
amazing_string(str,str1,str2)