# Assignment 10 # ไม่กำหนดจุดเริ่มต้นและสิ้นสุด , การป้อนตัวเลขอย่างไม่จำกัด
sum = 0 
while sum!=100: # หาผลรวมได้เรื่อยๆ ตราบใดที่ผลรวมไม่เท่ากับ 100
    number=int(input("ป้อนตัวเลขของคุณ : "))
    sum+=number
    print("ผลรวม =",sum)


while sum<100: # หาผลรวมได้เรื่อยๆ ตราบใดที่ผลรวมไม่มากกว่า 100
    number=int(input("ป้อนตัวเลขของคุณ : "))
    sum+=number
    print("ผลรวม =",sum)


while True: # หาผลรวมได้เรื่อยๆ ตราบใดที่ผลรวมไม่มากกว่า 100
    number=int(input("ป้อนตัวเลขของคุณ : "))
    sum+=number
    if sum>100:
        break
    print("ผลรวม =",sum)