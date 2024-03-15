n = int(input())
p = input().split()
i = 0

for j in range(0, n):
    i += int(p[j])

a = i/n
print(a)