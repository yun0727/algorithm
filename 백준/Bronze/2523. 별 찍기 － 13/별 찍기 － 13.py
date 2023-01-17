n=int(input())
for i in range(1,n):
    star="*"*(i)
    print(f"{star}")
print("*"*n)
for i in range(1,n):
    star="*"*(n-i)
    print(f"{star}")