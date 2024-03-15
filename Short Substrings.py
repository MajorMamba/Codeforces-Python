n = int(input())
for i in range(n):
    a = ""
    s = list(input())
    for i in range(len(s)):
        if i%2!=0:
            a+=s[i-1]
    a+=s[-1]
    print(a)

