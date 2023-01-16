while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    elif a*(b//a) == b:
        print('factor')
    elif b*(a//b) == a:
        print('multiple')
    else:
        print('neither')
