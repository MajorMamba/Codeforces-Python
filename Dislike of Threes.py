t = int(input())
for i in range(t):
    n = int(input())
    s = 1
    j=1
    while j<n:
        s+=1
        if s%3==0 or s%10==3:
            continue
        j+=1
    print(s)