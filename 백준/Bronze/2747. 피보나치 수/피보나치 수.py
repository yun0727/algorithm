n=int(input())
num=[1,1]
for i in range(2,n):
    number=num[i-2]+num[i-1]
    num.append(number)
print(num[-1])