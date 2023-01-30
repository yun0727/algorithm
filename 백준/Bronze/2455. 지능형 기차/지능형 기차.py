passenger=[]
initial=0
for i in range(4):
    out,comein=map(int,input().split())
    initial=initial+comein-out
    passenger.append(initial)
print(max(passenger))