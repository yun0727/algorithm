
import sys
input=sys.stdin.readline
n=int(input())
stack=[]
for i in range(n):
    a=list(map(str,input().split()))
    if a[0] == 'push':
        stack.append(int(a[1]))
    elif a[0]=='top':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    elif a[0]=='size':
        print(len(stack))
    elif a[0]=='empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop(-1))
            