n=int(input())
for i in range(n):
    password=input()
    if len(password)>=6 and len(password)<=9:
        print("yes")
    else:
        print("no")