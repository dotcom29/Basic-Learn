# ชื่อตัวแปร = ค่าที่เก็บในตัวแปร
x = 10 #integer
print(x)
x = 10 #integer => string
print("ผลลัพธ์ = " + str(x)) #แปลงเป็น string โดยใช้ str

x = 10
y = 3.99
z = True
print("ผลลัพธ์ = " + str(x))
print(y)
print(z)

#วิธีเช็คชนิดข้อข้อมูลของตัวแปร
x = 10
y = 3.99
z = True
print(type(x))
print(type(y))
print(type(z))
print(type("dotcom"))