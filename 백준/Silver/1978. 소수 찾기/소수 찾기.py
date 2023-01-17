n=int(input())
m=[]
count=[]
m=input().split()
sum=0
for i in range(n): #i=0,1,2,3
    number=int(m[i])
    for j in range(2,number): 
        if number % j == 0:
            count.append(j)
            break
if "1" in m:
    print(n-len(count)-1)
else:
    print(n-len(count))