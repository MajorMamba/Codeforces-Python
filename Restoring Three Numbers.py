s = input().split()
abc = 0
for i in s:
    if int(i)>abc:
        abc=int(i)
s.remove(str(abc))
ab = int(s[0])
bc = int(s[1])
ac = int(s[2])
c = abc-ab
b = abc-ac
a = abc-bc
print(a, b, c)