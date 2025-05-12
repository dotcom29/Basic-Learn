# break-หยุด / continue-กระโดดข้าม

# break
# การใช้ลูบ while

# ตัวอย่างที่ 1 print("จบโปรแกรม")
i=1
while i<=10:
    print("รอบที่ =",i)
    i+=1
print("จบโปรแกรม")

# ตัวอย่างที่ 2 เพิ่ม else
i=1
while i<=10:
    print("รอบที่ =",i)
    i+=1
else:
    print("จบโปรแกรม")

# ตัวอย่างที่ 3 หาก i=5 จะหยุดทันที
i=1
while i<=10:
    print("รอบที่ =",i)
    i+=1
    if(i==5):
          break
else:
    print("จบโปรแกรม")



# continue
#ตัวอย่างที่ 1 กำหนดให้ข้ามเลข 5
i=0
while i<=10:
     i+=1
     if(i==5):
          continue
     print("รอบที่ =",i)

print("จบโปรแกรม") #ที่มันจบด้วยเลข 11 เพราะเราไปใส่ i+=1 ก่อนที่จะทำการแสดงผล

#ตัวอย่างที่ 2 การหาค่าที่เป็นเลขคู่ โดยกระโดดข้ามตัวที่เลข 2 หารไม่ลงตัว
i=1
while i<10: # หากใส่ i<10 เฉยๆจะไม่มีเลข 11 ติดมาด้วย
     i+=1
     if(i%2 !=0):
          continue
     print("รอบที่ =",i)

print("จบโปรแกรม")

# การใช้ loop for
# กรณีหาเลขคี่
for i in range(1,11):
     if(i%2 == 0):
        continue
     print(i)
print("จบโปรแกรม")

for i in range(1,11):
     print(i)
     if(i==5):
          break
print("จบโปรแกรม")