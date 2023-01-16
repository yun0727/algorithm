n=int(input())
result=[]
for i in range(n):
    num=list(map(int,input().split()))
    if num[0] > num[1]-num[2]:
        print("do not advertise")
    elif num[0] == num[1]-num[2]:
        print("does not matter")
    elif num[0] < num[1]-num[2]:
        print("advertise")