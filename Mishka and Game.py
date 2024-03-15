t = int(input())
mi = 0
cr = 0
for i in range(t):
    m,c=input().split()
    if int(m)>int(c):
        mi += 1
    elif int(m)<int(c):
        cr += 1
if mi>cr:
    print("Mishka")
elif cr>mi:
    print("Chris")
elif mi==cr:
    print("Friendship is magic!^^")