n = int(input())
m = 0
for i in range(0,n):
    c = int(input())
    if c%2 == 0:
        m = (c/2)-1
    if c%2 != 0:
        m = ((c-1)/2)
    print(int(m))

