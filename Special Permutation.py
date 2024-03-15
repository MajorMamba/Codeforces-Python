t = int(input())
for i in range(t):
    n = int(input())
    s = ""
    for i in range(2, n+1):
        s+=str(i)+" "
    s += "1"
    print(s)