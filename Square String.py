t = int(input())
for i in range(t):
    s = input()
    if len(s)%2==0:
        ns = ''
        c = int(len(s)/2)
        for j in range(c):
            ns += s[j]
        if s.count(ns)==2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')   