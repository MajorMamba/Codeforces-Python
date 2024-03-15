n = int(input())
s = input().split()
t = []
r = []
o = []
d = [s.count("1"), s.count("2"), s.count("3")]
m = d[0]
for a in d:
    if a<m:
        m=a
if "1" in s:
    f = s.index("1")
if "2" in s:
    g = s.index("2")
if "3" in s:
    h = s.index("3")
if "1" in s:
    for i in s[s.index("1"):]:
        if i!="1":
            f += 1
        if i == "1":
            f += 1
            t.append(f)
if "2" in s:       
    for j in s[s.index("2"):]:
        if j!="2":
            g += 1
        if j == "2":
            g += 1
            r.append(g)
if "3" in s:        
    for k in s[s.index("3"):]:
        if k!="3":
            h += 1
        if k == "3":
            h += 1
            o.append(h)
print(m)
if m>0:
    for e in range(m):
        print(t[0], r[0], o[0])
        t.remove(t[0])
        r.remove(r[0])
        o.remove(o[0])   