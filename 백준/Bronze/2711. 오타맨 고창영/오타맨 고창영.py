t=int(input())
words=[]
for i in range(t):
    num,word=map(str,input().split())
    num=int(num)-1
    word=list(word)
    word.pop(num)
    print("".join(word))