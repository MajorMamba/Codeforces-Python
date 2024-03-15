n = (input())
m = (input())
b = ""
for i in range(0, len(n)):
    if m[i] != n[i]:
        b += "1"
    elif m[i] == n[i]:
        b += "0"

print(b)
    

