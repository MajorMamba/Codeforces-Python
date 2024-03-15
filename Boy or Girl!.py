inp = input()

i=0
s=""

for x in inp:
    if inp.index(x)==i:
        s +=x
    i +=1


y = len(s)

if  y%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")