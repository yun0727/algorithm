time=[]
start=[]
time=input().split(":")
start=input().split(":")
timesec=int(time[0])*3600+int(time[1])*60+int(time[2])
startsec=int(start[0])*3600+int(start[1])*60+int(start[2])
if startsec>timesec:
    resultsec=startsec-timesec
    h=resultsec//3600
    m=(resultsec%3600)//60
    s=(resultsec%3600)%60
    print("%.2d:%.2d:%.2d"%(h,m,s))
elif startsec<timesec:
    resultsec=startsec-timesec
    h=resultsec//3600
    m=(resultsec%3600)//60
    s=(resultsec%3600)%60
    print("%.2d:%.2d:%.2d"%(h+24,m,s))