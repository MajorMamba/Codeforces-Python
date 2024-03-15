n = int(input())
t = input().split()
c = 0
f = 0
for i in t:
    j = int(i)
    if j<0:
        if f == 0:
            c+=j
        if f>0:
            f+=j
    if j>0: 
        f+=j
print(c*-1)
