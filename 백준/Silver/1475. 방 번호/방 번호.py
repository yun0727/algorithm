n=(input())
num=[0]*10
for i in range(len(n)):
    num[int(n[i])] +=  1
if num[6] == 0 and num[9]==0:
    print(max(num))
elif (num[6]+num[9])%2==1:
    a=num[6]+num[9]
    num[6]=(a+1)//2
    num[9]=(a+1)//2
    print(max(num))
elif (num[6]+num[9])%2==0:
    a=num[6]+num[9]
    num[6]=(a)//2
    num[9]=(a)//2
    print(max(num))