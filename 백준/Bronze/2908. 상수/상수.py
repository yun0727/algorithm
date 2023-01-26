num1,num2=map(str,input().split())
third1=num1[0]
first1=num1[2]
num1=first1+num1[1]+third1
third2=num2[0]
first2=num2[2]
num2=first2+num2[1]+third2
if num1>num2:
    print(num1)
else:
    print(num2)