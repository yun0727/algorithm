n=int(input())
for i in range(1,n):
    star="*"*(i)
    blanc=" "*(2*(n-i))
    print(f"{star}{blanc}{star}")
print("*"*(2*n))
for i in range(1,n):
    star="*"*(n-i)
    blanc=" "*(2*(i))
    print(f"{star}{blanc}{star}")