c = input().split()
h = 0
u = 0

for i in c:
    if c.index(i) != h:
        u += 1
    h+=1
print(u)
