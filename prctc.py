nums = [2,7,11,15]
target = 9
class sloution(object):
    def twosum(self, nums, target):
        num1 = []
        for i in nums:
            num1.append(int(i))
        num2 = []
        pos1 = 0
        pos2 = 0
        posl = []
        brk = False
        for j in num1:
            ind = num1.index(j)
            for k in num1[ind+1:]:
                num2.append(k)
                if j+k == target:
                    pos1 = num1.index(j)
                    pos2 = num2.index(k)+1
                    posl.append(pos1)
                    posl.append(pos2)
                    brk = True
                    break
            if brk:
                break
        print(posl)
            
