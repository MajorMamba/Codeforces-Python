w = int(input())

s = 0

while w != 0:
    if w >= 5:
        w = w-5
        s += 1
    elif w >= 4:
        w = w-4
        s += 1
    elif w >= 3:
        w = w-3
        s += 1
    elif w >= 2:
        w = w-2
        s += 1
    elif w >= 1:
        w = w-1
        s += 1

print(s)