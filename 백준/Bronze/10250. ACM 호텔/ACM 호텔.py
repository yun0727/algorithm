t=int(input())
for i in range(t):
    h,w,n=map(int,(input().split()))
    floor=str(n%h)
    if floor =="0":
        floor=str(h)
        room=str(n//h)
    else:
        room=str((n//h)+1)
    if len(room) == 1:
        room= '0'+room
    print(floor+room)