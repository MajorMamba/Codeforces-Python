def Collatz_Conjecture():
    q = int(input("Please choose a positive number 'x';(x > 0): "))
    while q<=0:
        q = int(input("You are said to choose a positive number 'x'; (x > 0): "))
    print()
    print("The Collatz Conjecture of the number", q, "is given below:-")
    print()
    max = 0
    step = 0
    max_step = 0
    while q!=1:
        if q%2==0:
            q= int(q/2)
            step += 1
            if q>max:
                max=q
                max_step = step
        elif q%2!=0:
            q = (q*3)+1
            step += 1
            if q>max:
                max=q
                max_step = step
        print("Height = ", q, " Step =", step)
    print()
    print("Max height: ", max)
    print()
    print("Max height reached in step: ", max_step)
    print()
    print("Steps needed to reach the '4 2 1 loop': ", step)
    print()
print("The Collatz Conjecture : \n\nThe Collatz Conjecture is the simplest math problem no one can solve...\n\nThe process : \n\nIn this process you have to choose a positive number first.If your number is odd, then\nthe number will be multiplied with 3 and then 1 will be added to your number......\n\nFor example:- if you choose 7 then it will be (7 x 3) + 1 = 22.\n\nIn other hand if the number is even, then it will be divided by 2. \n\nFor example:- if you choose 30 it will be then (30 ÷ 2) = 15.\n\nNow the whole process runs like a loop.\n\nFor example:- if you choose the number '3'...being odd it will rise to (3 x 3) + 1 = 10 at first.\nthen 10 being even it will fall down to (10 ÷ 2) = 5, then the process will go on untill the number falls down to 1.\n\nThe 4 2 1 loop : \n\nThe rise and fall will stop form here as it becomes a loop now. See now the number is 1 so\n as it is odd it will rise to 4 by the rule...then 4 will be fall down to 2 and 2 will be down to 1.\n\nIt will happen again and again.No one has been able to establish a formula to solve this problem\nand that's why it is called 'The simplest unsolved math'\n\nSo I have programmed something where you can find how many steps will it take to reach the '4 2 1 loop',\nhow many steps were needed for reaching the max height and here you can find the rise and the fall of the number as height.\n\nEnjoy... =)\n\n")
Collatz_Conjecture()
Ans = input("Do you want to choose one more number? (Reply with 'yes' or 'no') : ")
Ans = Ans.lower()
while Ans == "yes":
    print()
    Collatz_Conjecture()
    Ans = input("Do you want to choose one more number? (Reply with 'yes' or 'no') : ")
else:
    quit = input("Press q and then 'Enter' to quit...")