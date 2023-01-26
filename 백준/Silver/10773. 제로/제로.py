k=int(input())
num=[]
for i in range(k):
    a=int(input())
    if a == 0:
        num.pop(-1)
    elif a !=0:
        num.append(a)
print(sum(num))