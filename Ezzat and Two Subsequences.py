t = int(input())
for i in range(t):
    n = int(input())
    s = input().split()
    j = []
    for k in s:
        j.append(int(k))
    l = max(j)
    s = 0
    for o in j:
        s += o
    s -= l
    s /= (len(j)-1)
    print(l+s)