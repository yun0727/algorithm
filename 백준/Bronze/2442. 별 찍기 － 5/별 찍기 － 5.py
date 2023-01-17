n=int(input())
for i in range(1,n+1):
    blanc=" "*(n-i)
    star="*"*(2*i-1)
    print(f"{blanc}{star}")