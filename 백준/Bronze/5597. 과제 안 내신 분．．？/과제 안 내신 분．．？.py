#과제 안 내신 분..?
# st=list(range(1,31))
st=[]
num=[]
for i in range(28):
    i=int(input())
    num.append(i)
for i in range(1,31):
    if i not in num:
        st.append(i)
print(min(st))
print(max(st))