n,k =input().split()


for i in range(1, int(k)+1):
    a = int(n)%10
    if a == 0:
        n = int(n)/10
    elif a != 0:
        n = int(n)-1

print(int(n))
    