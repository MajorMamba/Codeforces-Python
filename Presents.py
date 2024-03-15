n = int(input())
p = input().split()
s = ""
f = []
for i in range(1, n+1):
    f.append(i)
for j in f:
    s+=(str(p.index(str(j))+1)+" ")
print(s)