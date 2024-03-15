n = int(input())
x = input().split()
y = input().split()
j = 0
for i in range(1,n+1):
    if str(i) in x[1: ] :
        j += 1
    elif str(i) in y[1: ]:
        j += 1
if j == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")