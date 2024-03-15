s = ""
for i in range(5):
    m = input().split()
    for j in m:
        s+= j
k = s.index("1")
if k==0 or k==4 or k==20 or k==24:
    print("4")
if k==1 or k==3 or k==21 or k==23 or k==5 or k==9 or k==15 or k==19:
    print("3")
if k==2 or k==22 or k==10 or k==14 or k==6 or k==8 or k==16 or k==18:
    print("2")
if k==7 or k==11 or k==13 or k==17:
    print("1")
if k==12:
    print("0")



    