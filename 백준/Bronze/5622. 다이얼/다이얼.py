word=input()
word=list(word)
time=0
for i in range(len(word)):
    if word[i] == "A" or word[i] == "B" or word[i]=="C":
        time+=3
    elif word[i] == "D" or word[i] == "E" or word[i]=="F":
        time+=4
    elif word[i] == "G" or word[i] == "H" or word[i]=="I":
        time+=5
    elif word[i] == "J" or word[i] == "K" or word[i]=="L":
        time+=6
    elif word[i] == "M" or word[i] == "N" or word[i]=="O":
        time+=7
    elif word[i] == "P" or word[i] == "Q" or word[i]=="R" or word[i]=="S":
        time+=8
    elif word[i] == "T" or word[i] == "U" or word[i]=="V":
        time+=9
    elif word[i] == "X" or word[i] == "W" or word[i]=="Y" or word[i]=="Z":
        time+=10
print(time)