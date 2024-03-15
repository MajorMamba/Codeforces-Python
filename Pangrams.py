n = int(input())
a = input()
b =a.lower()
s = ""
m = 0
c = ""
j = 0
for i in b:
    if b.index(i) == m:
        c += i
    m +=1
for i in range(97, 123): 
    s += chr(i)
if len(c) == len(s):
    print("YES")
else:
    print("NO")