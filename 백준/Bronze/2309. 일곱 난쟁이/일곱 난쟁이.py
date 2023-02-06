num=[]
a=0
b=0
for i in range(9):
    num.append(int(input()))
for i in range(9):
    for j in range(i+1,9):
        if (num[i]+num[j])==(sum(num)-100):
            a=num[i]
            b=num[j]
num.remove(a)
num.remove(b)
num.sort()
for i in range(7):
    print(num[i])