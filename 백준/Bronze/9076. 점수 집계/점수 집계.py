t=int(input())
for i in range(t):
    score=list(map(int,input().split()))
    score.sort()
    score.remove(score[0])
    score.remove(score[3])
    if score[2]-score[0] >=4:
        print("KIN")
    else:
        print(sum(score))