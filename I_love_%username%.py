n = int(input())
c = input().split()
m = int(c[0])
l = int(c[0])
k = 0
for i in c:
    if int(i)>m:
        m=int(i)
        k += 1
    if int(i)<l:
        l=int(i)
        k += 1
print(k)
