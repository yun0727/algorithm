#OX 퀴즈
n=int(input())
result=[]
for i in range(n):
    score=0
    con=0
    ox=list(input())
    for i in ox:
        if i =='O':
            con+=1
            score+=con
        else:
            con=0
    result.append(score)
for i in range(n):
    print(result[i])
