t = int(input())
for i in range(t):
    n = int(input())
    s = input().split()
    m = int(n/2)
    p = int((n-1)/2)
    ns = []
    fr = ''
    if n%2==0:
        for j in range(m):
            ns.append(s[j])
            ns.append(s[(n-1)-j])
    else:
        for k in range(p):
            ns.append(s[k])
            ns.append(s[(n-1)-k])
        ns.append(s[p])
    for o in ns:
        fr += str(o)+' '
    print(fr)