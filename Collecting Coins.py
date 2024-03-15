t = int(input())
for i in range(t):
    a,b,c,N = input().split()
    f = 0
    n = int(N)
    if int(a)>=int(b) and int(a)>=int(c):
        f = int(a)
    elif int(b)>=int(a) and int(b)>=int(c):
        f = int(b)
    elif int(c)>=int(b) and int(c)>=int(a):
        f = int(c)
    if int(a)<f:
        n-=f-int(a)
    if int(b)<f:
        n-=f-int(b)
    if int(c)<f:
        n-=f-int(c)
    if n>=0:
        if n%3==0 or n==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")