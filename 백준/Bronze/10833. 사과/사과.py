n=int(input())
div=[]
for i in range(n):
    student,apple=map(int,input().split())
    div.append(apple%student)
print(sum(div))