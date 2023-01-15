t=int(input())
for i in range(t):
    a1,b1=map(int,input().split())
    a2,b2=map(int,input().split())
    a3,b3=map(int,input().split())
    a4,b4=map(int,input().split())
    a5,b5=map(int,input().split())
    a6,b6=map(int,input().split())
    a7,b7=map(int,input().split())
    a8,b8=map(int,input().split())
    a9,b9=map(int,input().split())
    A=a1+a2+a3+a4+a5+a6+a7+a8+a9
    B=b1+b2+b3+b4+b5+b6+b7+b8+b9
    if A>B:
        print("Yonsei")
    elif A<B:
        print("Korea")
    else:
        print("Draw")