n=int(input())
k=[]
result=[]
for i in range(n):
    k.append(int(input()))
if k.count(1) >k.count(0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
