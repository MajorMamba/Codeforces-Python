n = int(input())
s = 1
m = []
for i in range(n):
    M = int(input())
    m.append(M)
b = m[0]
for j in m:
   if j!=b:
        s+=1
        b=j
print(s) 