y, w = input().split()
d = max(int(y),int(w))
f = (6-d)+1
if f%2==0 and int(f/2)!=3:
    print(str(int(f/2))+"/"+"3")
elif f%2==0 and int(f/2)==3:
    print("1/1")
elif f%3==0:
    print(str(int(f/3))+"/"+"2")
else:
    print(str(f)+"/"+"6")
