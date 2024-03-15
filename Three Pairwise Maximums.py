t = int(input())
for i in range(t):
    s= input().split()
    l = []
    for j in s:
        l.append(int(j))
    if l.count(max(l))==2:
        print("YES")
        if s.index(str(min(l)))==0:
            print(min(l), min(l), max(l))
        elif s.index(str(min(l)))==1:
            print(min(l), max(l), min(l))
        elif s.index(str(min(l)))==2:
            print(max(l), min(l),min(l))
    elif l.count((max(l)))==3:
        print("YES")
        print(max(l), max(l),max(l))
    else:
        print("NO")        