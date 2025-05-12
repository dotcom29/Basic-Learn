# pass #การข้ามหัวข้อนั้นไปก่อน #มีไว้เพื่อวางโครงสร้างของโค้ด
age=int(input("ป้อนอายุของคุณ : "))

if age<=15:
    if age==15:
        pass
    elif age==14:
        pass
    else :
        print("ประถมศึกษา")
else :
    print("ม.ปลาย")

print("จบโปรแกรม")