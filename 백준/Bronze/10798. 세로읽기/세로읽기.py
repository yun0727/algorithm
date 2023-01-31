matrix=[]
result=""
length=[]
for i in range(5):
    line=list(input())
    matrix.append(line)
    length.append(len(matrix[i]))
for i in range(5):
    if len(matrix[i])<max(length):
        while len(matrix[i]) < max(length):
            matrix[i].append("")
for i in range(max(length)):
    for j in range(5):
        result += (matrix[j][i])
print(result) 