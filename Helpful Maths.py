s = input()

sp = s.split("+")
ns = ""

a = sp.count("1")
b = sp.count("2")
c = sp.count("3")

for i in range(a):
    ns += "1"
for i in range(b):
    ns += "2"
for i in range(c):
    ns += "3"

ns = list(ns)

print("+".join(ns))