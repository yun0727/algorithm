while True:
    a=int(input())
    if a== -1 :
        break
    re=[]
    for i in range(1,a):
        if a%i == 0:
            re.append(i)
    if sum(re) == a:
        print(a," = "," + ".join(str(i) for i in re),sep="")
    else:
        print(f"{a} is NOT perfect.")
