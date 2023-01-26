n=int(input())
sum=n
for i in range(n):
    str=[]
    word=input()
    word=list(word)
    sen=word
    for k in range(len(sen)-1):
        if sen[k] == sen[k+1]:
            pass
        elif sen[k] in sen[k+1:]:
            sum-=1
            break
print(sum)