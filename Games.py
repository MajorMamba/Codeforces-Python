n = int(input())
m = 0
A = []
B = [] 
for i in range(0, n):
    a,b= input().split()
    A.append(a)
    B.append(b)
for i in A:    
        m += B.count(i)
print(m)