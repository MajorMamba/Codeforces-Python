t = input()
h = input().split()
f = ""
for i in h:
    f+=i
if t[0] in f or t[1] in f:
    print("YES")
else:
    print("NO")