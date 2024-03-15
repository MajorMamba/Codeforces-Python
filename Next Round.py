n, k = input().split()
nth = input().split()

nr = 0

for i in range(0, int(k)):
    if int(nth[i])<=0:
        nr += 0
    else:
        nr += 1
    

for i in range(int(k), int(n)):
    if int(nth[i])>0 and nth[i] == nth[int(k)-1]:
        nr += 1
print(nr)
