start = int(input("ใส่แม่สูตรคูณเริ่มต้น : "))
stop  = int(input("ใส่แม่สูตรคูณสุดท้าย : "))
for x in range(start, stop+1):
    print("สูตรคูณแม่ =",x)
    for y in range(1, 13):
        print(x, "X", y, "=", (x*y))

for x in range(-stop, -start+1):
    print("สูตรคูณแม่ =",-x)
    for y in range(-12, 0):
        print(-x, "X", -y, "=", (x*y))

