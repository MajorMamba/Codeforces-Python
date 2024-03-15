n= int(input())
l = 1
for i in range(2, n):
    if n%i==0:
        l+=1
print(l)    