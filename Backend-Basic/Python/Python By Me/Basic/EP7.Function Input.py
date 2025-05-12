#Basic
input("กรุณาป้อนชื่อของท่าน : ") #function นี้จะเห็นข้อมูลเป็น str ทั้งหมด

#การเก็บข้อมูลลงในตัวแปร
name = input("กรุณาป้อนชื่อของท่านอีกครั้ง : ") #รับค่าที่ผู้ใช้ป้อนแล้วเก็บลงตัวแปร name
print("ชื่อของคุณคือ = " +name)

#การใส่ข้อมูลแบบ str
fname=input("กรุณาป้อนชื่อขอท่าน : ")
lname=input("กรุณาป้อนนามสกุลของท่าน : ")
print("ชื่อของคุณคือ = "+fname)
print("นามสกุลของคุณคือ = "+lname)

#การใส่ข้อมูลแบบ int แต่ funtion เห็นข้อมูลเป็น str
x=input("ป้อนตัวเลขตัวที่ 1 : ")
y=input("ป้อนตัวเลขตัวที่ 2 : ")
#process
z=x+y
#output
print(z)

#อยากให้ข้อมูลเป็น int
#วิธีแรก
x=input("ป้อนตัวเลขตัวที่ 1 : ")
y=input("ป้อนตัวเลขตัวที่ 2 : ")
#process
z=int(x)+int(y)
#output
print(z)

#วิธีสอง + รวบ process & output
x=int(input("ป้อนตัวเลขตัวที่ 1 : "))
y=int(input("ป้อนตัวเลขตัวที่ 2 : "))
#process + output
print(x+y)