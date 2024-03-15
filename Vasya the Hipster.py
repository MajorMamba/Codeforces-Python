R,B = input().split()
r = int(R)
b = int(B)
f = 0
u = 0
if r>=b:
    for i in range(b):
        r -= 1
        b -= 1
        f += 1
elif b>r:
    for i in range(r):
        r -= 1
        b -= 1
        f += 1
if r>0:
    u = int(r/2)
if b>0:
    u = int(b/2)
print(f, u)
