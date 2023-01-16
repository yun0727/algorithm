str=list(input())
sum=10
for i in range(1,len(str)):
    if str[i-1] == str[i]:
        sum+=5
    elif str[i-1] != str[i]:
        sum += 10
print(sum)