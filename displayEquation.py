num = -210
while num<1100:
    display = ""
    if (num < 0):
        print("The argument should be non-negative.")
    elif (num >= 1000):
        print("The argument should be less than 1000.")
    elif (num >= 0 and num < 1000):
        if (num == 0):
            display = "{0} = 1 * {0}".format(num)
        elif (num <10):
            display = "{0} = 1 * {0}".format(num)
        elif ( num >=10 and num <100):
            if (num%10 == 0):
                display = "{0} = 10 * {1}".format(num, (num//10))
            else:
                display = "{0} = 10 * {1} + 1 * {2}".format(num, (num//10), (num%10))
        elif (num >= 100 and num <1000):
            if (num%100 == 0):
                display = "{0} = 100 * {1}".format(num, (num//100))
            elif (num %100 < 10 and num%100 > 0):
                display = "{0} = 100 * {1} + 1 * {2}".format(num, (num//100), (num%10))
            elif (num%10 == 0):
                display = "{0} = 100 * {1} + 10 * {2}".format(num, (num//100), (num//10)%10)
            else:
                display = "{0} = 100 * {1} + 10 * {2} + 1 * {3}".format(num, (num//100), (num//10)%10, (num%10))
        print(display)
    num += 1