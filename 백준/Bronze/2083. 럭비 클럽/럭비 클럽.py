name,age,weight=input().split()
while name!="#" and age!="0" and weight!="0":
    if int(age) >17 or int(weight)>=80:
        print(name,"Senior")
        name,age,weight=input().split()
    else:
        print(name,"Junior")
        name,age,weight=input().split()