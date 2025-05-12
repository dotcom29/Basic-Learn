# เจาะลึก string(Note.String)
# การเข้าถึง String
name="dotcom studio 23" # index คือตำแหน่งของตัวอักษร => เริ่มที่ 0,1,2,3,...(รวมช่องว่างด้วย)
print(name[0]) 
print(name[1])
print(name[2])

print(name[0:3]) #นับถึงแค่ 2 ตัวแรก
print(name[0:4])
print(name[:4])

print(name[-2]) #เครื่องหมายลบคือนับจากด้านหลัง

print("อายุเท่าไหร่ :",name[:-3]) #สองภาพนี้ต่างกันแค่เครื่องหมาย :
print("อายุเท่าไหร่ :",name[-3:])


# len Function จำนวนความยาวของ String (รวมช่องว่าง)
print(len(name))


# strip Function
name = " dotcom " #มีช่องว่างซ้ายและขวา
print(name)
print(len(name))

name = name.strip()
print(name) #ไม่มีช่องว่างซ้ายและขวา
print(len(name))

# ต้องการลบช่องว่างด้านซ้าย
name = " dotcom "
name = name.lstrip()
print(name) #ไม่มีช่องว่างด้านซ้าย
print(len(name))

# ต้องการลบช่องว่างด้านขวา
name = " dotcom "
name = name.rstrip()
print(name) #ไม่มีช่องว่างด้านขวา
print(len(name))


# แปลง case ของ string
name = "dOtCoM"
print(name.upper()) #แปลงข้อความเป็นตัวพิมพ์ใหญ่
print(name.lower()) #แปลงข้อความเป็นตัวพิมพ์เล็ก
print(name.capitalize()) #แปลงข้อความหน้าสุดเป็นตัวพิมพ์ใหญ่


# การแทนที่
name = "dotcom เกรด 4 อยู่ชั้นปีที่ 4 และอยู่ซอย 4"
print(name.replace("4","2.5",1)) # การใส่เลข 1 คือการนับแค่อันดับแรก(ในกรณีที่มีเลขซ้ำกัน)
print(name.replace("4","2.5",2)) # การใส่เลข 2 คือการนับแค่อันดับสอง(ในกรณีที่มีเลขซ้ำกัน)


# การเช็คข้อความ
name = "ไปซื้อข้าวและอาหารที่ตลาด"
x = "ข้าว" in name # การเช็คคำว่า "ข้าว" ในตัวแปล name
y = "ไข่" in name # การเช็คคำว่า "ข้าว" ในตัวแปล name
print(x)
print(y)

if x :
    name = name.replace("ข้าว","ไข่")
print(name)


# การต่อ string
fname = "thanakrit"
lname = "sittipanya"
age = "23"
fullname = fname+lname+age

print(fullname)
print("ชื่อต้น : "+fname+"\tนามสกุล : "+lname+"\tอายุ : "+age)


# การจัดรูปแบบการแสดงผล(Function Format)
fname = "thanakrit"
lname = "sittipanya"
age = "23"
salary = 500.98755

text = "ชื่อต้น:{}\tนามสกุล:{}\tอายุ:{}" 
print(text.format(fname,lname,age))

text = "ชื่อต้น:{0}\tนามสกุล:{1}\tอายุ:{2}\tอาชีพ:{3}\tเงินเดือน{4:.2f}" # สามารถระบุตำแหน่งได้ #(:.2f คือการระบุทศนิยม 2 ตำแหน่ง
print(text.format(fname,lname,age,"โปรแกรมเมอร์",salary))



# การนับจำนวนคำในประโยค(Count)
fruit = "ไปซื้อผลไม้ มีทุเรียน มังคุด ข้าวเหนียวทุเรียน ที่ตลาด"
print(fruit.count("ทุเรียน"))



# เช็คคำขึ้นต้น
name = "นายกอไก่ ใจดี"
print(name.startswith("นาย"))

# การกำหนดคำสั่ง
if name.startswith("นาย"):
    print("เป็นเพศชาย")
else :
    print("เป็นบุลคลอื่น")

# การเช็คคำลงท้าย
name = "1125669"

if name.endswith("0"): # หากลท้ายด้วย 0 จะถูกหวย
    print("ถูกหวย")
else :
    print("ไม่ถูกหวย")