# Assigntment9 # การกำหนดจุดเริ่มต้นและจุดสิ้นสุด
start , stop = 1,3
sum , avg = 0,0 # กำหนดให้ค่า sum , avg เริ่มต้นเท่ากับ 0
while (start<=stop):
    number=int(input("ป้อนตัวเลขของคุณ :"))
    sum+=number # บวกเลขที่ป้อนแต่ละรอบ
    start+=1

avg = sum/stop
print("ผลรวม =",sum)
print("ค่าเฉลี่ย =",avg)