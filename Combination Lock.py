n = int(input())
l = input()
u = input()
k = 0
for i in range(n):
    c=int((max(l[i], u[i])))-int((min(l[i], u[i])))
    if c<=5:
        k += c
    elif c >5:
        k += 10-c
print(k)