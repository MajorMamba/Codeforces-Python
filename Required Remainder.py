t = int(input())
for i in range(t):
    x,y,n = input().split()
    j = int(n)
    while (j%int(x))!=int(y):
        j-=1
    print(j):
            