t = int(input())
for i in range(t):
    m = int(input())
    n = input().split()
    for j in n:
        if n.count(j)==1:
            print(n.index(j)+1)