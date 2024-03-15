n,h = input().split()
he = input().split()

v = 0

for i in range(0, int(n)):
    if int(he[i]) <= int(h):
        v += 1
    else:
        v += 2

print(v)



