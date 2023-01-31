t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    matrix=[]
    sum=0
    for j in range(m):
        line=list(input().split())
        matrix.append(line)
    box=[]
    for k in range(n):
        line=[]
        for l in range(1,m+1):
            line.append(matrix[-l][k])
        box.append(line)
    for a in range(n):
        index=0
        for b in range(m):
            if box[a][b] == '1':
                index += b
        count=box[a].count('1')
        index_sum=0
        for c in range(count):
            index_sum += c
        sum += index-index_sum
        # print(index_sum)
        # print(count)
        # print(index)  
    print(sum)