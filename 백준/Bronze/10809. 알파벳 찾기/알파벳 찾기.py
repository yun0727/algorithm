#알파벳 찾기
words=input()
for i in range(97,123):
    print(words.find(chr(i)),end=" ")