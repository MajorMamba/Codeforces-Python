n,k = input().split()
t = input().split()
T = []
for i in t:
    if int(i)+int(k)<=5:
        T.append(int(i))
print(int((len(T))/3))