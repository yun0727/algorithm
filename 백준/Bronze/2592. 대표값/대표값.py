num=[]
count=[]
for i in range(10):
    num.append(int(input()))
for j in range(10):
    count.append(num.count(num[j]))
    result=count.index(max(count))
print(sum(num)//10)
print(num[result])