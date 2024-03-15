s = input()
d="abcdefghijklmnopqrstuvwxyz"
r = 0
f = "a"
for i in s:
    c =max(d.index(f), d.index(i))-min(d.index(f), d.index(i))
    if c+1>13:
        r += 26-c
    else:
        r+=c
    f=i
print(r)