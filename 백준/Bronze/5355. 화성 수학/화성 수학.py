t=int(input())
result=[]
for i in range(t):
    num=input().split()
    for j in range(1,len(num)):
        if num[j]=="@":
            num[0] = float(num[0]) * 3
        elif num[j] == "%":
            num[0] = float(num[0]) + 5
        elif num[j] == "#":
            num[0] = float(num[0])-7
    result.append(num[0])
for i in range(t):
    print("%.2f"%result[i])