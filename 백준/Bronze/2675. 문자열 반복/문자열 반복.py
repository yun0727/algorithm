t=int(input())
result=[]
for i in range(t):
    a,b=input().split() # 3 ABC
    text=""
    for i in b:
        text+=(i*int(a))
    print(text)