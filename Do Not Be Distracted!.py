t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    t = []
    t.append(s[0])
    g = 0
    for j in range(1, len(s)):
        if s[j-1] != s[j] and s[j] not in t:
            t.append(s[j-1])
        if s[j-1] == s[j]:
            t.append(s[j-1])
        if s[j-1] != s[j] and s[j] in t:
            g +=1                    
    if g>0:
        print("NO")
    else:
        print("YES")           