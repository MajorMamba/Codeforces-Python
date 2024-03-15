t = int(input())
for i in range(t):
    k = input()
    w = input()
    c = 0
    for j in range(len(w)-1):
        a = 0
        a = int(k.index(w[j]))-int(k.index(w[j+1]))
        if a<0:
            a *= -1
        c+=a
    print(c)