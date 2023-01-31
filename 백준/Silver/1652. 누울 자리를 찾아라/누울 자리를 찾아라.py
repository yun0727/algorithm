n=int(input())
matrix=[]
split=[]
a=0
b=0
for i in range(n):
    line=(input())
    matrix.append(line) 
for i in range(n):
    split.append(matrix[i].split('X'))
    for j in range(len(split[i])):
        if len(split[i][j]) >=2:
            a+=1
split=[]
box=[]
for k in range(n):
    line=''
    for l in range(1,n+1):
        line+=(matrix[-l][k])
    box.append(line)
for i in range(n):
    split.append(box[i].split('X'))
    for j in range(len(split[i])):
        if len(split[i][j]) >=2:
            b+=1    
print(a,b)