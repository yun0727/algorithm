t=int(input())
score=[]
scores=[]
max_result=[]
for i in range(t):
    n=int(input())
    for j in range(n):
        score.append(input().split())
        scores.append(int(score[j][0]))
        max_score=max(scores)
    max_index=int(scores.index(max_score))
    max_result.append(score[max_index][1])
    print(max_result[i])
    score=[]
    scores=[]