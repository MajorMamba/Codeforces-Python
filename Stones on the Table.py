nos =  int(input())
cos = input()
 
s = 0
 
for i in range (1, nos):
    if cos[i-1] == cos[i]:
        s += 1
 
print(s)