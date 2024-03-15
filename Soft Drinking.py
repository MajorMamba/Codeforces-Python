n, k, l, c, d, p, nl, np= input().split()
s = []
s.append(int(((int(k)*int(l))/int(nl))))
s.append(int(c)*int(d))
s.append(int(int(p)/int(np)))
print(int(min(s)/int(n)))