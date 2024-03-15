n = int(input())
s = input().split()
b = 0
c = int(s[0])
t = []
o = []
for i in s:
    if int(i)>b:
        b=int(i)
    if int(i)<c:
        c=int(i)
f = s.index(str(b))
g = s.index(str(c))
for j in s[f:]:
    if j != str(b):
        f +=1
    else:
        f+=1
        t.append(f)
for k in s[g:]:
    if k != str(c):
        g += 1
    else:
        g+=1
        o.append(g)
u = 0
if int(t[0])>int(o[-1]):
    u = (int(t[0])-1)+(n-((int(o[-1])+1)))
elif int(t[0])<int(o[-1]):
    u = (int(t[-0])-1)+(n-(int(o[-1])))
print(u)