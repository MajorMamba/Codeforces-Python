t = int(input())
for i in range(t):
    n = int(input())
    s = 0
    b = 0
    l = []
    for j in range(1, n+1):
        l.append(2**j)
    if n!=2:
        for k in l[:int((n/2)-1)]:
            b+=k
    else:
        s += l[0]
    if n!=2:
        b+=l[-1]
    if n!=2:
        for h in l[int((n/2)-1):len(l)-1]:
            s+=h
    elif n==2:
        b+=l[-1]
    print(b-s)