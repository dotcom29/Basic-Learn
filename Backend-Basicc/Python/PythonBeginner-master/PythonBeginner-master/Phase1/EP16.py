# if ซ้อน if
age=int(input("ป้อนอายุของคุณ : "))

if age<=15: # หากเงื่อนไขบรรทัดนี้เป็นจริง จะไปเช็คข้างในอีกที
    if age==15:
        print("ม.3")
    elif age==14:
        print("ม.2")
    elif age==13:
        print("ม.1")
    else :
        print("ประถมศึกษา")
else :
    print("ม.ปลาย")

print("จบโปรแกรม")


age = int(input("กรุณาป้อนอายุของท่าน : "))
if age>=13:
    if age==15:
        print("ม.3")
    elif age==14:
        print("ม.2")
    elif age==13:
        print("ม.1")
    elif age>=16 and age<=19:
        print("ม.ปลาย")
    else:
        print("มหาลัยวัวชน")

else:
    print("ชั้นประถม")