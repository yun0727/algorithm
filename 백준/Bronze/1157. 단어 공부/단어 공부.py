word=input()
word=word.lower()
alphabet="abcdefghijklmnopqrstuvwxyz"
co={}
for i in range(0,26):
    if alphabet[i] in word:
        co[alphabet[i].upper()]=word.count(alphabet[i])
max_list=list(co.values())
max_value=max(max_list)
max_alphabet=list(co.keys())
if max_list.count(max_value)>1:
    print("?")
else:
    print(max_alphabet[max_list.index(max_value)])