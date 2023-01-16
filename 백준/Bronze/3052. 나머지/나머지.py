#나머지
num=[]
value=[]
for i in range(10):
    i=int(input())
    num.append(i)
for i in range(10):
    value.append(num[i]%42)
value=set(value)
print(len(value))