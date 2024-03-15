n = int(input())
a = 0
b = 0

for i in range(0, n):
    m = int(input())
    if m%3 == 0:
        a = int(m/3) 
        b = int(m/3)
    elif (m+1)%3 == 0:
        a = int(m/3)
        b = int(m/3)+1
    elif (m-1)%3 == 0:
        a = int(m/3)+1
        b = int(m/3)
    print(a, b)