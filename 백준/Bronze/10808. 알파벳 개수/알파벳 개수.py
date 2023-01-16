s=input()
alphabet=("abcdefghijklmnopqrstuvwxyz")
result=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(26):
    sum=0
    for j in range(len(s)):
        if s[j]==alphabet[i]:
            sum+=1
            result[i] = sum
for i in range(26):
    print(result[i],end=" ")