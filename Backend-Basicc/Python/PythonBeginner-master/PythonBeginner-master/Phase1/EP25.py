# โครงสร้างควบคุมแบบทำซ้ำ (while loop)
# ลูป while ใช้เมื่อไม่มีกำหนดรอบที่ชัดเจน

"""
while   expression :
        statment
"""

i=1 # ตัวนับจำนวนรอบ
while i<=3: # หากไม่เข้าเงื่อนไขในนี้ โปรแกรมจะจบการทำงานทันที เช่น i>3
    print("รอบที่ ",i)
    i=i+1 # การเพิ่มค่า i


i=1 #ค่าเรื่มต้นของ i = 1
summation = 0 #เก็บผลการบวกเลขตามจำนวนรอบ โดยเริ่มต้นเท่ากับ 0
average = 0 #ผลรวม / จำนวนรอบ
while i<=5:
    summation+=i #เก็บผลรวมของ i แต่ละรอบ
    print("รอบที่",i,"ค่า sum = ",summation)
    i+=1
average = summation/5
print("ผลรวมการบวกเลข = ",summation)
print("ค่าเฉลี่ย = ",average)



i=1 #ค่าเรื่มต้นของ i = 1
summation = 0 #เก็บผลการบวกเลขตามจำนวนรอบ โดยเริ่มต้นเท่ากับ 0
average = 0 #ผลรวม / จำนวนรอบ
count=int(input("ระบุจำนวนรอบ : "))
while i<=count:
    summation+=i #เก็บผลรวมของ i แต่ละรอบ
    print("รอบที่",i,"ค่า sum = ",summation)
    i+=1
average = summation/count
print("ผลรวมการบวกเลข = ",summation)
print("ค่าเฉลี่ย = ",average)


# ลูป for ใช้เมื่อมีกำหนดรอบที่ชัดเจน
for i in range(3) : # range คือ กำหนดรอบ , range มีอยู่ 3 พารามิเตอร์ คือ(start,stop,step) , การใช้ range จะเริ่มต้นด้วย 0 เสมอ
    print("ครั้งที่ 1 :""รอบที่ =",i,"Hello World")

for i in range(5) :
    print("ครั้งที่ 2 :""รอบที่ =",i+1,"Hello World") #เราสามารถบวก 1 เข้าไปได้เพื่อไม่ให้เริ่มต้นด้วย 0

for i in range(1,7,2) : # เราสามารถระบุเลขเริ่มต้นได้,ระบุเลขที่จะหยุดได้,ระบุเลขขั้นต่อไปได้ (start,stop,step)
    print("ครั้งที่ 3 :""รอบที่ =",i+1,"Hello World")


# การหาค่า SUM
summation=0
for i in range(1,11): #summation
    summation+=i
    print("รอบที่ =",i,"sum =",summation)

print("ผลรวม =",summation)
print("เฉลี่ย =",summation/10) # ค่าเฉลี่ยหาร 10 เพราะกำหนดค่าถึง 10

# การระบุตัวเลขติดลบ
for i in range(-10,5):
    print("รอบที่ :",i)

for i in range(10,0,-1):
    print("นับถอยหลังใน :",i)