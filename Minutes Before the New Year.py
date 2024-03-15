t = int(input())
for i in range(t):
    h,m = input().split()
    s = 0
    s += (23-int(h))*60
    s += 60-int(m)
    print(s)