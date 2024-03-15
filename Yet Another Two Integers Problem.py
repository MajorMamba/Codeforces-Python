n = int(input())
for i in range(n):
    f = 0
    A,B = input().split()
    a = int(A)
    b = int(B)
    c = 0
    if a<b:    
        c = b-a
        f += int(c/10)
        c = c%10
        if c>0:
            f += 1
    if a>b:    
        c = a-b
        f += int(c/10)
        c = c%10
        if c>0:
            f += 1
    print(f)