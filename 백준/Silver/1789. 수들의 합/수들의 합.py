s=int(input())
sum=0
# sum(1+2+3+4+5+6+7+8+9+10 66 78 91 105 120 136 153 171 190 210)
for i in range(1,s+1):
    sum=0.5*(i)*(i+1)
    if sum>s:
        print(i-1)
        break
    elif sum == s:
        print(i)
        break