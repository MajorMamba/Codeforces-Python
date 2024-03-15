t = int(input())
for i in range(t):
    n,k = input().split()
    s = input().split()
    d = 1
    for j in range(1, len(s)):
        if int(s[j]) < int(s[j-1]):
            d+=1
    if d==int(k):
        print("YES")
    else:
        print("NO"):