t= int(input())
for i in range(t):
    b = 0
    c = 0
    n = int(input())
    s = input().split()
    for j in s:
        if int(j)>b:
            b=int(j)
    for k in s:
        if int(k)>c and int(k)<b:
            c = int(k)
    if c == 0:
        c = int(k)
    print(b*c) 
