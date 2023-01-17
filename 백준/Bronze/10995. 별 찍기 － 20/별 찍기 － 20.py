n=int(input())
m=n
for i in range(n):
    if i %2 == 0:
        print("* "*m)
    elif i%2==1:
        print(" *"*m)