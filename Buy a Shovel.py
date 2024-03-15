k,r = input().split()
f = 1
while (int(k)*f)%10!=0 and ((int(k)*f)-int(r))%10!=0:
    f+=1
print(f)