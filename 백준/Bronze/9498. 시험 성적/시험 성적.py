a=int(input())
if a>=90 and a<=100:
    score='A'
elif a>=80 and a<=89:
    score='B'
elif a>=70 and a<=79:
    score='C'
elif a>=60 and a<=69:
    score='D'
else:
    score='F'
print(score)