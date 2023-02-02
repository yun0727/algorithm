passenger=[0]
for i in range(10):
    a,b=map(int,input().split())
    passenger.append(passenger[i]+b-a)
print(max(passenger))
