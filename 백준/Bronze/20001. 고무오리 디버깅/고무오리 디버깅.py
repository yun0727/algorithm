begin=input()
sum=0
while True:
    question=input()
    if question == "고무오리 디버깅 끝":
        break
    else:
        if question == "문제":
            sum+=1
        elif question == "고무오리":
            if sum==0:
                sum+=2
            else:
                sum -=1
if sum == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")