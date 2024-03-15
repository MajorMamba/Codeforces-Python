t = int(input())
for i in range(t):
    n = int(input())
    s = input().split()
    k = 0
    l = 0
    if "1" not in s:
            if s.count("2")%2==0:
                print("YES")
            else:
                print("NO")
    elif "2" not in s:
            if s.count("1")%2==0:
                print("YES")
            else:
                print("NO")
    else:
        for j in s:
            if "1" in s and "2" in s:
                k += int(j)
        if k%2==0:
            print("YES")
        else:
            print("NO")