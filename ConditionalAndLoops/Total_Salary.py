list1=[ item for item in input().split()]
for i in range(0,len(list1)):
    if i==0:
        list1[i]=int(list1[i])
        basic=list1[i]
    else:
        grade=list1[i]
        break

hra=float((20/100)*basic)
da=float((50/100)*basic)
pf=float((11/100)*basic)
if grade=='A':
    allow=1700
    totalsal=round(float(basic+allow+hra+da-pf))
elif grade=='B':
    allow=1500
    totalsal=round(float(basic+allow+hra+da-pf))
else:
    allow=1300
    totalsal=round(float(basic+allow+hra+da-pf))
print(totalsal)