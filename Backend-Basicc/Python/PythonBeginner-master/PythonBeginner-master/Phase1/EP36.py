# เกมทายเลขลูกเต๋า
# 1,2,3,4,5,6 => ความเป็นไปได้ 6 อย่าง

import random
#สุ่มเลขลูกเต๋า
myrandom = random.randrange(1,7) # 1 - 6
k=1 #โอกาสในการสุ่มตัวเลข
correct=False #กำหนดค่าที่ถูกต้องข้างนอกลูปด้วย
print("คุณมีโอกาสตอบ 3 ครั้ง \n")
print(myrandom) # หากอยากรู้เฉลยสามารถ print เฉลยได้เลย
while True: #สามารถรับค่าได้เรื่อยๆ
    number=int(input("ป้อนคำตอบของคุณ = "))
    correct=(number==myrandom) # correct = true / false
    if not correct : #คำใบ้หากตอบไม่ถูก
        if(number>myrandom):
            print("ตัวเลขที่ถูกมีค่าน้อยกว่านี้")
        if(number<myrandom):
            print("ตัวเลขที่ถูกมีค่ามากกว่านี้")

    if correct :
        print("ตอบถูกรับไปเลย 1 ล้านบาท")
        break
    if number<0 or k==3: # k คือโอกาสตอบ 3 ครั้ง หากเกิน จะออกจากลูป
        break
    k+=1

if not correct :
    print("เสียใจด้วยนะ")
    print("เฉลย =" , myrandom)
