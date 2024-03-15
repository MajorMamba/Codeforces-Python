pob,ash,nob = input().split()

count = 0

for i in range(1, int(nob)+1):
    a = int(pob)*i
    count = count+a

c = count-int(ash)

if c>=0:
    print(c)
else:
    print(0)

