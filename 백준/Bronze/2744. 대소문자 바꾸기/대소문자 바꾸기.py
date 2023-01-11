#대소문자 바꾸기
str=list(input())
for i in range(len(str)):
    if str[i] == str[i].upper():
        str[i]=str[i].lower()
    elif str[i] == str[i].lower():
        str[i]=str[i].upper()
for i in range(len(str)):
    print(str[i],end="")
