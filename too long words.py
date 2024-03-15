x = input("number: ")

def cl(x):
    lc = 0
    for le in x:
        if le.isalpha():
            lc+=1
    return lc

linx = cl(x)
line = (x[0]+str(linx)+x[-1])
print(line)

if linx >= 10 and x != int():
    print(line)
else:
    print(x)
