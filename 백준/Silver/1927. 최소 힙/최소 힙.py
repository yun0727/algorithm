import heapq
import sys
input=sys.stdin.readline
x=int(input())
heap=[]
for _ in range(x):
    temp=int(input())
    if temp == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,temp)