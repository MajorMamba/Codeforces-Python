n = int(input())
m = 0
h = 0
for i in range(0, n):
    a, b = input().split()
    h = int(b)-int(a)+h
    if h>m:
        m=h
print(m)
