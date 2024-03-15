t = int(input())
for i in range(t):
    n = input()
    s = 0
    if len(n)==1:
        s+=(int(n)-1)*10
        for l in range(1, len(n)+1):
            s+=l
    elif len(n)==2:
        s+=int((int(n)-11)/10)*10
        for g in range(1, len(n)+1):
            s+=g
    elif len(n)==3:
        s+=int((int(n)-111)/100)*10
        for f in range(1, len(n)+1):
            s+=f
    elif len(n)==4:
        s+=int((int(n)-1114)/1000)*10
        for h in range(1, len(n)+1):
            s+=h
    print(s) 