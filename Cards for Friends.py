t = int(input())
for i in range(t):
    W, H, N = input().split()
    w = int(W)
    h = int(H)
    n = int(N)
    s = 1
    if w%2==0:
        while w%2==0:
            s *= 2
            w /= 2
    if h%2==0:
        while h%2==0:
            s *= 2
            h /= 2            
    if s>=n:
        print("YES")
    else:
        print("NO")