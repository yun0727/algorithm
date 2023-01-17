l=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
kor=a//c+1
math=b//d+1
if a%c ==0:
    kor=a//c
if b%d ==0:
    math=b//d
if kor>math:
    study=kor
elif kor<=math:
    study=math
print(l-study)