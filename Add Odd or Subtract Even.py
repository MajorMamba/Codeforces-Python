t = int(input())
for i in range(t):
    a,b = input().split()
    if int(b)>int(a):
        if (int(b)-int(a))%2==0:
            print("2")
        else:
            print("1")
    elif int(a)>int(b):
        if (int(a)-int(b))%2==0:
            print("1")
        else:
            print("2")
    else:
        print("0")