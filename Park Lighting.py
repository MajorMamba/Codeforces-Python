t = int(input())
for i in range(t):
    n,m = input().split()
    s = 0
    if int(n)%2==0:
        s = int((int(n)/2)*int(m))
    elif int(m)%2==0:
        s = int((int(m)/2)*int(n))
    else:
        if int(n)==1:
           s = int(((int(int(m)/2)+1)*int(n))) 
        elif int(n)>int(m):
            s = int(((int(int(n)/2)+1)*int(m)))-1
        else:
            s = int(((int(int(m)/2)+1)*int(n)))-1
    print(s):