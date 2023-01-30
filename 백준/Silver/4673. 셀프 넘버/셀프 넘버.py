def d(n):
    n=n+sum(map(int,str(n)))
    return n
non_self_num=set()
for i in range(1,10001):
    non_self_num.add(d(i))
for j in range(1,10001):
    if j not in non_self_num:
        print(j)