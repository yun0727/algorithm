a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=list(map(int,input().split()))
result=[]
result.append(sum(a))
result.append(sum(b))
result.append(sum(c))
result.append(sum(d))
result.append(sum(e))
score=max(result)
winner=result.index(score)+1
print(winner,score)