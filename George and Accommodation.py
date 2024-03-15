n = int(input())

r = 0

for i in range (0, n):
    p,q = input().split()
    if int(q) - int(p) >= 2:
        r +=1
print(r)   