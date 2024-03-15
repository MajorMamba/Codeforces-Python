t = int(input())
for i in range(t):
    n,x = input().split()
    s = 1
    if int(n)>2:
        a = 2
        while a<int(n):
            a+=int(x)
            s+=1
    print(s)