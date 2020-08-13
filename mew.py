
import random
myrandom = random.randrange(1,7)
k=0
while True:
    number = int(input("ป้อนคำตอบของคุณ : "))
    if number<0 or k==2:
        print("เสียใจด้วย กลับบ้านไปนะจ๊ะ")
        break
    correct=(number==myrandom) #true/false
    if not correct:
        if(number>myrandom):
            print("น้อยกว่านี้อีกนิด")
        if(number<myrandom):
            print("มากกว่านี้อีกหน่อย")
    if correct:
        print("รับรางวัลไปเลย 1000M!!!")
        break

    k+=1