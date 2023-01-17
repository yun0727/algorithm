t=int(input())
score=[]
scores=[]
max_result=[]
for i in range(t):
    n=int(input())
    for j in range(n):
        score.append(input().split())
        scores.append(int(score[j][1])) #10,30,20
        max_score=max(scores) #30
    max_index=int(scores.index(max_score))
    max_result.append(score[max_index][0])
    print(max_result[i])
    score=[]
    scores=[]