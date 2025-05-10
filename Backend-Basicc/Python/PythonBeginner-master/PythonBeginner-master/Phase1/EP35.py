# สร้างขอบตาราง

"""
xxx      => ปกติ
xxx
xxx
xxx
"""

"""
xxxx     => เฉพาะขอบ
x  x
x  x
x  x
xxxx
"""

number=int(input("ป้อนขนาด  = ")) 
for row in range(number) :
    for column in range(number):
        if row==0 or row==number-1 or column==0 or column==number-1:
           print("x",end="")
        else:
            print(" ",end="") # เว้นช่องว่างในกรณีที่เงื่อนไขไม่เป็นจริง เช่น เมื่อกำหนด column==0 ก็คือ column แรกต้องปริ้น x หากเป็น column อื่นจะเป็นช่องว่างเปล่า 
    print(" ")


# การกำหนด row==0 คือกำนหดให้ print x ได้เมื่อแถวแรกเท่ากับ 0 ซึ่งโปรแกรมกำหนดให้แถวแรกเท่ากับ 0 เสมอ
"""
เมื่อใส่เลข 10 ผลลัพธ์คือ 
xxxxxxxxxx





"""
# ส่วนการกำหนด row==number-1 คือกำหนดให้ปริ้น x ลงในบรรทัดสุดท้าย ตัวสุดท้ายก็คือตัวเลขที่เราใส่ลงไป
"""
เมื่อเราใส่เลข 10 ผลลัพธ์คือ


xxxxxxxxxx
"""
