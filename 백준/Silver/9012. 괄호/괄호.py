t=int(input())
for i in range(t):
    case=input()
    case=list(case)
    sum=0
    for i in case:
        if i=='(':
            sum+=1
        elif i==')':
            sum-=1
        if sum<0:
            print('NO')
            break
    if sum>0:
        print("NO")
    elif sum==0:
        print('YES')