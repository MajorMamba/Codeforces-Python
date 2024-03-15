a,b,c,d = input().split()
s = input()
e = 0
for i in s:
    if int(i)==1:
        e+=int(a)
    if int(i)==2:
        e+=int(b)
    if int(i)==3:
        e+=int(c)
    if int(i)==4:
        e+=int(d)
print(e)