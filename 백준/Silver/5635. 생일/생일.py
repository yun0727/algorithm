n=int(input())
name=[]
ages=[]
for i in range(n):
    name.append(input().split())
    age=(2000-int(name[i][3]))*372+(372-(((int(name[i][2])-1)*31)+int(name[i][1])))
    ages.append(age)
    young=min(ages)
    old=max(ages)
    youngin=ages.index(young)
    oldin=ages.index(old)
print(name[youngin][0])
print(name[oldin][0])