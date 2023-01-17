m=int(input())
n=int(input())
result=[]
for i in range(1,101):
    if i**2>=m and i**2<=n:
        result.append(i**2)
if len(result)==0:
    print(-1)
else:
    print(sum(result))
    print(min(result))