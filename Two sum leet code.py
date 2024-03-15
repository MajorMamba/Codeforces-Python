nums = input().split(',') # Without brackets
target = int(input())
num1 = []
for i in nums:
    num1.append(int(i))
pos1 = 0
pos2 = 0
posl = []
brk = False
for j in num1:
    num2 = []
    ind = num1.index(j)
    for k in num1[ind+1:]:
        num2.append(k)
        if j+k == target:
            pos1 = num1.index(j)
            if num1.index(j) == 0:
                pos2 = num2.index(k)+num1.index(j)+1
            else:
                if num2.index(k) == 0:
                    pos2 = num2.index(k)+num1.index(j)+1
                else: 
                    pos2 = num2.index(k)+num1.index(j)+1
            posl.append(pos1)
            posl.append(pos2)
            brk = True
            break
    if brk:
        break
print(num1, "\n", num2, "\n", posl)