t = int(input())
for i in range(t):
    a,b = input().split()
    c = int(a)
    d = int(b)
    if c>d:
        c+=d
        d=c-d
        c=c-d
    c*=2
    if c>d:
        print(c**2)
    else:
        print(d**2)