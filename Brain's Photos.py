n, m = input().split()
b = ""
for i in range(int(n)):
    s=input().split()
    b += str(s)
if "C" in b or "M" in b or "Y" in b:
    print("#Color")
else:
    print("#Black&White")