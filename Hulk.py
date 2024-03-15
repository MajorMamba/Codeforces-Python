n = int(input())
f = 1
a = n%2
b = "it "
c = "that "
d = "I hate "
e = "I love "
s = ""
while f<=n:
    if f>1 and s.count(d)>s.count(e):
        s += e+c
    elif f>1 and s.count(d) == s.count(e):
        s += d+c
    if f==n and s.count(d)==s.count(e):
        s+= d+b
    elif f==n and s.count(d)>s.count(e):
        s+= e+b        
    
    f += 1
print(s)

