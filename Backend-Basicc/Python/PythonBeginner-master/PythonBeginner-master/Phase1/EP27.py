#Assignment 9
# แม่สูตรคูณ

for x in range(2,13):
    print("แม่ =",x)
    for y in range(1,13):
            print(x,'x',y,"=",(x*y))

# ให้ผู้ใช้งานใส่ตัวเลขเอง
start=int(input("ป้อนแม่สูตรคูณเริ่มต้น = ")) # 1
stop=int(input("ป้อนแม่สูตรคูณสุดท้าย = ")) # 4

for x in range(start,stop+1): #การบวก 1 คือเราจะได้ค่าที่ต้องการเป๊ะๆ
    print("แม่ = ",x)
    for y in range(1,13):
        print(x,'x',y ," = ",(x*y))
