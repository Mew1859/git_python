
import random
myrandom = random.randrange(1,7)
k=1
while True:
    number = int(input("ป้อนคำตอบของคุณ : "))
    if number<0 or k==3:
        print("ไปเรียนมาใหม่")
        break
    correct=(number==myrandom) #true/false

    if not correct:
        if(number>myrandom):
            print("น้อยกว่านี้อีกนิด")
        if(number<myrandom):
            print("มากกว่านี้อีกหน่อย")
            
    if correct:
        print("ถูกสักที")
        break

    k+=1