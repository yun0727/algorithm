str=input()
for i in range(1,len(str)//10+2):   
    print(str[(i-1)*10:(i*10)])