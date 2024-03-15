t = int(input())
for i in range(t):
    n = int(input())
    if n<=0:
        print("0")
    if n<=6 and n>0:
        print("15")
    if n<=8 and n>6:
        print("20")
    if n<=10 and n>8:
        print("25")
    elif n>10:    
        if n%6==0 or n%8 == 0 or n%10 == 0:
            print(int(n/2)*5)
        elif n%6!=0 and n%8 != 0 and n%10 != 0:
            while n%2!=0:
                n+=1
            print(int(n/2)*5)  