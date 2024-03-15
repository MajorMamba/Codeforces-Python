w = input()
u = 0
l = 0

for i in w:
    if i.isupper() == True:
        u += 1
    else:
        l += 1

if u>l:
    print(w.upper())
elif u<=l:
    print(w.lower())
