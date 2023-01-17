n=int(input())
for i in range(1,n+1):
    star="*"*(2*(n-i)+1)
    blanc=" "*(i-1)
    print(f"{blanc}{star}")