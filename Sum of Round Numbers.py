t = int(input())
for i in range(t):
    n = int(input())
    s = str(n)
    Sum_count = 0
    k = "" 
    for j in range(len(s)):
            if int(s[j]) != 0:
                k += str(int(s[j])*(10**(len(s)-j-1)))
                k += " "
                Sum_count += 1
    print(Sum_count)
    print(k)