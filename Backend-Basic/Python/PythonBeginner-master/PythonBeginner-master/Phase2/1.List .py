# การเขียนแบบ primitive (Note.non Primitive)
a=1
a1=2
a2=3
a3=4
a4=5
a5=6
a6=7

# การเขียนแบบ non-primitive : list(สามารถเก็บข้อมูลได้ทั้ง Boolean,String,Number,Bytes)
number=[] # การสร้าง list ว่าง
number=[1,2,3,4,5,6] # list มีสมาชิก 1-6
name=["นาย A ","นาย B ","นาย C "] # list name มีสมาชิกเป็นข้อความ
all=[10,"นายไข่",True,3.14,-10]
# Construtor => การนิยาม
name=list(["นาย A","นาย B" ,"นาย C"])
# การแสดงผล
print(name) # โปรแกรมจะปริ้นในบรรทัดล่าสุด
print(all)
print(number)
# การเข้าถึงข้อมูลของ List , การระบุ index
print(number[0]) # index ที่ 0
print(number[1]) # index ที่ 1
print(number[2]+number[0]) # การบวกเลข
print(name[2])
print(all[-3])
print(all[1:3]) # ตัวเลข 3 คือก่อนถึงลำกับที่ 3 = 2
print(all[-3:-1])
print(all[1:]) # การไม่ระบุตัวเลขสุดท้าย คือ เอาตัวเลขทั้งหมดที่มี

# การแก้ไขข้อมูล
number=[1,2,3,4,5,6]
# ชื่อตัวแปร [index] = "ข้อมูลที่แก้ไข"
print("ก่อนแก้ไข => ",number)
number[2]=9 # แก้ไขจาก index ที่ 2 = 3 ไปเป็นตัวเลข 9
number[5]=10 # แก้ไขจาก index ที่ 5 = 6 ไปเป็นตัวเลข 10
number[-1]="นายไข่" # แก้ไขจาก index ตัวสุดท้าย ไปเป็นข้อความ
print("หลังแก้ไข => ",number)

# การแสดงผลด้วย Loop
number=[1,2,3,4,5,6]
for x in number:
    print("สมาชิก",x)

sum=0
for x in number:
    sum+=x # sum=sum+x
print(sum)

sum=0
for item in number:
    sum+=item # item คือ การบวกแต่ละตัวเลข
print(sum)

sum=0
for item in number:
    print(item)

# การตรวจสอบ
number=[1,2,3,4,5,6]
fruit=["มะม่วง",",มะนาว","มะยม"]
if 20 in number: # 20 อยู่ในตัวแปร number ไหม
    print("อยู่")
else:
    print("ไม่อยู่")

# การใชช้ฟังก์ชั่น len() ทำงานร่วมกับ Loop for
fruit=["มะม่วง",",มะนาว","มะยม"]
for i in range(len(fruit)): # การทำงานร่วมกับ len(),เป็นการแสดงจำนวนตัวเลขตามคำที่อยู่ในตัวแปล fruit
    print(fruit)
    print(fruit(i)) # แสดงชื่อร่วมด้วย

for item in fruit: # ไม่ได้ทำงานร่วมกับ len()
    print(item)

# การเพิ่มข้อมูล (append,insert)
fruit=["มะม่วง",",มะนาว","มะยม"]
# append
print("ก่อนเพิ่มข้อมูล => ",fruit)
fruit.append("มะปราง") # การเพิ่มข้อมูล แต่นำข้อมูลมาต่อท้าย
print("หลังเพิ่มข้อมูล => ",fruit)
# insert
print("ก่อนแทรก => ",fruit)
fruit.insert(1,"ทุเรียน") # การเพิ่มข้อมูลไปในที่ที่เราได้กำหนด เช่น index ที่ 1
print("หลังแทรก => ",fruit)

# การลบข้อมูล
fruit=["มะม่วง",",มะนาว","มะยม"]
# remove
fruit.remove("มะยม") # เราสามารถระบุสมาชิกที่อยากลบออกได้
print("remove => ",fruit)
# pop
fruit.pop() # การลบข้อมูลล่าสุดออกไป (ตัวทางด้านขวามือสุด)
print("Pop => ",fruit)
# del
del fruit[1] # การระบุ index ที่เราอยากลบออกได้เลย
print(fruit) # เคลียร์หน่วยความจำ = ลบทั้งตัวแปร และ สมาชิก
del fruit
print(fruit) # ไม่มีข้อมูลแล้ว

fruit.clear() # ลบแค่สมาชิก
print(fruit)

# การคัดลอกข้อมูล
fruit=["มะม่วง",",มะนาว","มะยม"]
x=[]
print(x)
x=fruit.copy() # คัดลอกข้อมูลสมาชิกในตัวแปร fruit
print(x)

# การรวมข้อมูล
number=[1,2,3,4,5,6]
fruit=["มะม่วง",",มะนาว","มะยม"]

allGroup=number+fruit # การรวมกันโดยการสร้างตัวแปรใหม่
print(allGroup)

number.extend(fruit) # การนำสมาชิกในตัวแปร fruit เข้าไปในตัวแปร number
print(number)

# การค้นหาและนับจำนวน
number=[1,2,3,4,5,6,7,8,9,10,5,6,5,3]
x=number.count(5) # การค้นหาเลข 5 ว่าเจออยู่กี่จำนวน
print(x)

# Assignment 1 รับและเรียงลำดับข้อมูลตัวเลข
number=[]
while True: # รับข้อมูลได้ไม่จำกัด
    x=int(input("ป้อนตัวเลขของคุณ :"))
    if x<0:
        break
    number.append(x)

print("ก่อนเรียง=>",number)
number.sort()
print("น้อยไปมาก=>",number)
number.reverse()
print("มากไปน้อย=>",number)
print("จบโปรแกรม")

# Assignment 2 หาค่ามากสุด / ต่ำสุด / ผลรวม ตัวเลข
number=[]
while True:
    x=int(input("ป้อนตัวเลขของคุณ :"))
    if x<0:
        break
    number.append(x)

print(number)
print("ค่าที่น้อยที่สุด คือ ",min(number))
print("ค่าที่มากที่สุด คือ ",max(number))
print("ผลรวม คือ ",sum(number))

# Assignment 3 หากลุ่มเลขคู่ / เลขคี่
number=[]
odd=[] # สร้างตัวแปรเก็บข้อมูลเลขคี่
even=[] # สร้างตัวแปรเก็บข้อมูลเลขคู่
while True:
    x=int(input("ป้อนตัวเลขของคุณ :"))
    if x<0:
        break
    if x%2 == 0:
        even.append(x)
    else :
        odd.append(x)
    number.append(x)

print("ตัวเลขทั้งหมด =>" ,number)
print("เลขคู่ => ",even)
print("เลขคี่ => ",odd)

# Assignment 4 เรียงลำดับชื่อ
student=["สมพร","แก้ว","จอมขวัญ","อัมพร","ก้อง","กล้า"]

print(student) # ก่อนเรียง

student.sort()
print(student)

student.reverse()
print(student)

# Assignment 5 เรียงสมาชิกหลังสุด => หน้าสุด
fruit=["มะม่วง","มะยม","มะนาว","ทุเรียน"]

print(fruit) # ก่อนเรียง

fruit=fruit[::-1] # หลังเรียง
print(fruit)

# Assignment 6 หาค่าเลขยกกำลัง
number=[1,2,3,4,5,6,7]

print(number)

#แบบปกติ
for i in range(len(number)): # การเข้าถึงสมาชิดแต่ละ number เก็บลงไปที่ตัวแปร i
    number[i]=number[i]**2
print(number)

#แบบลดรูป
number=[i*i for i in number]
print(number)

# Assignment 7 จับคู่คำทักทาย / บุคคล

"""
greeting => Hi , Hello 

people => ก้อง , แก้ม

ผลลัพธ์ => Hi ก้อง , Hi แก้ม , Hello ก้อง , Hello แก้ม

"""

greeting=["สวัสดี","Hi", "Hello","Good Bye"]
people=["ก้อง","แก้ม","โจ้"]
result=[]

#แบบปกติ
for x in greeting:
    for y in people:
        result.append(x+y)
print(result)

#ลดรูป
result=[x+y for x in greeting for y in people]
print(result)

# Assignment 8 การจับคู่สินค้าและราคา

fruit=["มะม่วงดอง","แตงโมปั่น","ฝรั่งแซ่บ๊วย"]
price=[50,30,15]

for x,y in zip(fruit,price): # ฟังก์ชั่น zip คือการจับคู่สมาชิก โดยใช้ loop แค่ 1 ครั้ง
    print("สินค้า = ",x ,"ราคา = ",y)

for x,y in zip(fruit,price[::-1]): # เปลี่ยนราคาใหม่ จากหลัง => หน้า
    print("สินค้า = ",x , "ราคา = ",y)

# Assignment 9 การค้นหาและนับจำนวนตัวอักษรในสมาชิก

message=["aa","aab","cba","bba","aba","cca","aaa","aabaac"] # อยากทราบว่ามีตัว a กี่ตัวในสมาชิก
result=[]

for item in message: #ตั้งชื่อว่า item
    result.append(item.count("a"))
print(result)