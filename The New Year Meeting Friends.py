import abc


h= input().split()
b = 0
c = int(h[0])
for i in h:
    if int(i)>b:
        b=int(i)
    if int(i)<c:
        c = int(i)
d = int((b+c)/2)
print((b-d)+(d-c))


