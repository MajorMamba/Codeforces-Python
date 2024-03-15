n,m =input().split()
s =""
for i in range(1, int(n)+1):
    if i%2 != 0:
        for j in range(0, int(m)):
            s+="#"
        s += "\n"
    elif i%4!=0:
        for j in range(0, int(m)-1):
            s+="."
        s+="#"
        s+= "\n"
    else:
        s+="#"
        for j in range(1, int(m)):
            s+="."
        s+= "\n"
print(s)