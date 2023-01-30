m=int(input())
n=int(input())
number=[]
for i in range(m,n+1):
    zero=[]
    for j in range(2,i):
        zero.append(i%j)
    if 0 not in zero:
        number.append(i)
if 1 in number:
    number.remove(1)
if len(number) ==0:
    print(-1)
else:
    print(sum(number))
    print(min(number))