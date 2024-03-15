n,k = input().split()
m = 240-int(k)
f = 0
s = []
for i in range(1, int(n)+1):
    s.append(5*i)
for i in s:
    if i<=m:
        m -= i
        f += 1
print(f)