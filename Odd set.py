t = int(input())
for i in range(t):
    a = int(input())
    s = input().split()
    e = []
    o = []
    for j in s:
        if int(j)%2==0:
            e.append(j)
        else:
            o.append(j)
    if len(e)==len(o):
        print("YES")
    else:
        print("NO")