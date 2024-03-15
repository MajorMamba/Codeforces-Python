n = int(input())
c = input().split()
s = 0
d = 0
for i in range(len(c)):
    if int(c[0])>int(c[-1]):
        s+=int(c[0])
        c.remove(c[0])
    elif int(c[0])<int(c[-1]):
        s+=int(c[-1])
        c.remove(c[-1])
    if int(c[0])>int(c[-1]):
        d+=int(c[0])
        c.remove(c[0])
    elif int(c[0])<int(c[-1]):
        d+=int(c[-1])
        c.remove(c[-1])
if n%2!=0:
    s += int(c[-1])
else:
    d += int(c[-1])
print(s,d) 