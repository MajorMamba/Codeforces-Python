n = int(input())
s = input().split()
m = 1
k = [1]
for i in range(1,n):
    if int(s[i])>int(s[i-1]):
        m+=1
        k.append(m)
    else:
        m=1
print(max(k))