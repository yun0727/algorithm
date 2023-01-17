n=int(input())
for i in range(1,n):
    blanc=" "*(n-i)
    star="*"*(i)
    print(f"{blanc}{star}")
print("*"*n)
for i in range(1,n):
    blanc=" "*(i)
    star="*"*(n-i)
    print(f"{blanc}{star}")