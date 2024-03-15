t = int(input())
for i in range(t):
    s = input()
    a = s.count("A")
    b = s.count("B")
    c = s.count("C")
    if "A" in s and "B" in s and "C" in s:
        if a+c == b:
            print("YES")
        else:
            print("NO")
    elif "C" not in s:
        if a == b:
            print("YES")
        else:
            print("NO")
    elif "A" not in s:
        if c == b:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")