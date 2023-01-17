t=int(input())
grade=[]
score=[]
classes=[]
for i in range(t):
    n=int(input())
    for j in range(n):
        grade.append((input().split()))
        score.append(float(grade[j][1])*int(grade[j][0]))
        classes.append(int(grade[j][0]))
        total_grade=sum(score)
        total_classes=sum(classes)
    print(total_classes, round(total_grade/total_classes,1))
    grade=[]
    score=[]
    classes=[]
    total_grade=0