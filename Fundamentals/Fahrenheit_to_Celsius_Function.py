def printTable(start,end,step): 
    while start<=end:
        cel=int((start-32)*(5/9))
        print(start,'\t',cel)
        start=start+step

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)
