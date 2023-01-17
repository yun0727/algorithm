#5554 심부름 가는 길
hs=int(input())
sp=int(input())
pa=int(input())
ah=int(input())
sum=hs+sp+pa+ah
min=sum//60
sec=sum%60
print(min)
print(sec)