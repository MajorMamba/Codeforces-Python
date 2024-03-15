n =  int(input())
m = 0
for i in range(0, n):
    a = input()
    if a == "Tetrahedron":
        m += 4
    if a == "Cube":
        m += 6
    if a == "Octahedron":
        m += 8
    if a == "Dodecahedron":
        m += 12
    if a == "Icosahedron":
        m += 20
print(m)
    
    