n= int(input())
w = input().split()
m = 0
d = 0
for i in w:
    if int(i)>m:
        m = int(i)
for i in w:
    d += m-int(i)
print(d)