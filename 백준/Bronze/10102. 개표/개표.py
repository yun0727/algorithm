v=int(input())
vote=[]
vote=list(input())
if vote.count('A')>vote.count('B'):
    print('A')
elif vote.count('A')==vote.count('B'):
    print('Tie')
elif vote.count('A')<vote.count('B'):
    print('B')