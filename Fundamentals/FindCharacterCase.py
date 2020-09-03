char=str(input())
ordvalue=ord(char)
if ordvalue>=65 and ordvalue<=90:
    print("1")
elif ordvalue>=97 and ordvalue<=120:
    print('0')
else:
    print('-1')