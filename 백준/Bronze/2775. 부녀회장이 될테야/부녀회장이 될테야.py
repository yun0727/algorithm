t=int(input())
for i in range(t):
    k=int(input())
    n=int(input())
    f0=[i for i in range(1,n+1)]
    for j in range(k):
        matrix=[]
        for j in range(n):
            matrix.append(sum(f0[:j+1]))
        f0=matrix.copy()
    print(matrix[-1])