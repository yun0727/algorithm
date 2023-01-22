num=list(map(int,input().split()))
# for i in range(4):
#     if num[i]>num[i+1]:
#         big=num[i]
#         small=num[i+1]
#         num[i]=small
#         num[i+1]=big
#         print(num)
while num != [1,2,3,4,5]:
    for i in range(4):
        if num[i]>num[i+1]:
            big=num[i]
            small=num[i+1]
            num[i]=small
            num[i+1]=big
            for i in range(5):
                print(num[i],end=" ")
            print("")
            # print(num)