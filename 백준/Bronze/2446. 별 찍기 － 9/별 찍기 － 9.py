n=int(input())
for i in range(1,n):
    star="*"*(2*(n-i)+1)
    blanc=" "*(i-1)
    print(f"{blanc}{star}")
for i in range(n):
    blanc=" "*(n-1-i)
    star="*"*((2*i)+1)
    print(f"{blanc}{star}")