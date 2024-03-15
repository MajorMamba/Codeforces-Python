t = int(input())
f = 0
while f<t:
    c = 0
    a,b = input().split()
    v = int(a)%int(b)
    if v!=0:
        print(((int(int(a)/int(b))+1)*int(b))-int(a))
    else:
        print("0")
    f += 1
