t=int(input())
me=[]
dad=[]
for i in range(t):
    candy,people = map(int,input().split())
    me.append(candy//people)
    dad.append(candy%people)
for i in range(t):
    print(f"You get {me[i]} piece(s) and your dad gets {dad[i]} piece(s).")