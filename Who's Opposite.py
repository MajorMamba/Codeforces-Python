t = int(input())
for i in range(t):
    a,b,c= input().split()
    f = max(int(a),int(b))
    g = min(int(a),int(b))
    m = (f-g)*2
    k = (f-g)
    if m>=f and m>=int(c):
        if k+int(c)<=m:
            print(k+int(c))
        else:
            print(int(c)-k)
    else:
        print("-1")