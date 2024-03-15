n = int(input())
for i in range(n):
    j = 0
    b = 0
    t = int(input())
    if t%4!=0:
        print("NO")
    if t%4==0:
        s = []
        v = []
        for k in range(1, t+1):
            if k%2==0:
                j += k
                s.append(k)
        for l in range(1, t-1):
            if l%2!=0:
                b += l
                v.append(l)
        f=v[-1]                   
        while j!=(b+f):
            f+=2
        b += f
        v.append(f)                
        print("YES")
        r = ""                
        for o in s:
            r+=str(o)+" "
        for m in v:
            r+=str(m)+" "
        print(r)



