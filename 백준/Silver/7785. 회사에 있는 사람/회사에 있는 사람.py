n=int(input())
Name={}
for i in range(n):
    name, status=map(str,input().split())
    if status == "enter":
        Name[name] = 'enter'
    else:
        del Name[name]
result=sorted(Name.keys(),reverse=True)
for i in result:
    print(i)