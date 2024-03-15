n =int(input())
n = n+1
l=[]
s = 0
while len(l)!=4:
    l=[]
    for i in str(n):
        if i not in l:
            l.append(i)
    s = n        
    n+=1     
print(s)