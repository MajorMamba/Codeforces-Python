t = int(input())
for i in range(t):
    n = int(input())
    s = input().split()
    f = 0
    k = ""
    for j in s:
        if s.index(j)==f:
            k += j+" "
        f += 1
    print(k)