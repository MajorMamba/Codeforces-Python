n = int(input())
f = 0 
s = 0
g = -1
while f<n:
    for i in range(1, n+1):
        if f<=n:
            s += i
            f += s
            g += 1
if n!=1:
    print(g)
else:
    print(g+1)