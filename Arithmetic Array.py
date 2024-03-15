t = int(input())
for i in range(t):
    l = int(input())
    a = input().split()
    n = 0
    for j in a:
        n+= int(j)
    if n<0:
        print('1')
    if n==0:
        print('1')
    if n>0 and n>l:
        print(n-l)
    if n>0 and n<l:
        print('1')
    if n>0 and n==l:
        print('0') 