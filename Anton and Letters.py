n = str(input().split())
n = n.replace('{', '')
n = n.replace('}', '')
n = n.replace('[', '')
n = n.replace(']', '')
n = n.replace(',', '')
n = n.replace(' ', '')
n = n.replace('}', '')
n = n.replace("'", '')

f = 0
c = 0
n = list(n)
for i in n:
    if n.index(i) == f:
        c += 1
    f += 1
print(c)
