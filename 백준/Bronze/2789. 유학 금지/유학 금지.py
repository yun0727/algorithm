str=list(input())
cambridge=["C","A","M","B","R","I","D","G","E"]
result=''
for i in str:
    if i not in cambridge:
        result+=i
print(result)