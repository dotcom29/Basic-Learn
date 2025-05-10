# (Note.non Primitive)
# การเปรียบเทียบระหว่าง tuple กับ list
tup=(1,2,3,4,"dotcom","ส้ม",True,3.99) # tuple
lis=[1,2,3,4,"dotcom","ส้ม",True,3.99] # list
print(tup)
print(lis)

# Constructor => ใช้เพื่อระบุว่าข้อมูลนั้นจะเป็น list tuple หรืออื่นๆ และเราสามารถเปลี่ยนชนิดข้อมูลได้ เช่น tuple => list
tup=tuple((1,2,3,4,"dotcom","ส้ม",True,3.99)) # tuple
lis=list([1,2,3,4,"dotcom","ส้ม",True,3.99]) # list
print(tup)
print(lis)

# การเปลี่ยนข้อมูลผ่าน index
tup=(1,2,3,4,"dotcom","ส้ม",True,3.99) # tuple
lis=[1,2,3,4,"dotcom","ส้ม",True,3.99] # list
lis[0]="เชียงใหม่"
tup(0)="เชียงใหม่" # tuple ไม่สามารถเปลี่ยนแปลงข้อมูลได้
print(tup)
print(lis)

# การเข้าถึงข้อมูลผ่าน index
tup=(1,2,3,4,"dotcom","ส้ม",True,3.99)
print(tup(4)) # eror
print(tup[4]) # ต้องระบุ index ด้วยก้ามปู

# วิธีการแก้ข้อมูล tuple โดยใช้ Constructor
tup=(1,2,3,4,"dotcom","ส้ม",True,3.99)
lis=list(tup)
lis[0]="เชียงใหม่"
print(lis)
# แปลงกลับไปเป็น tuple เหมือนเดิม เพื่อไม่ให้เปลี่ยนแปลงข้อมูล
tup=tuple(lis)

# การปริ้นสมาชิกแต่ละตัว
tup=(1,2,3,4,"dotcom","ส้ม",True,3.99)
for item in tup:
    print("สมาชิก = ",item)

# การค้นหาคำที่ต้องการ
tup=(1,2,3,4,"dotcom","ส้ม",True,3.99)
if "ทุเรียน" in tup:
    print("เป็นสมาชิก")
else:
    print("ไม่เป็นสมาชิก")

# การกำหนดให้เป็น tuple
x=()
print(x)

x=tuple()
print(x)

x=("dotcom",)
print(x)

# การเพิ่มข้อมูล (เรียกว่า joy tuple)
name = ("dotcom","jojo") #tuple
new = "nut" #string  , ต้องแปลง nut => tuple
print(name)

name = ("dotcom","jojo") #tuple
new = ("nut",) # tuple
print(name)

# การแก้ไขข้อมูล
tup=(1,2,3,4,"dotcom","ส้ม",True,3.99)
city=["กรุงเทพ","ชลบุรี","เชียงใหม่"]

tup=tup+tuple(city)
print(tup)

# การลบข้อมูล
tup=(1,2,3,4,"dotcom","ส้ม",True,3.99)
print("Before",lis)
lis=list(tup) # แปลง tuple => list
lis.pop() # การลบข้อมูลหลังสุดออก
tup=tuple(lis)
print(tup)

tup=(1,2,3,4,"dotcom","ส้ม",True,3.99)
print("After",lis)
lis=list(tup) # แปลง tuple => list
lis.remove("ส้ม") # เลือกลบข้อมูลได้
tup=tuple(lis)
print(tup)

# การค้นหาและนับจำนวนสมาชิก
tup=(1,2,3,4,"dotcom","ส้ม",True,3.99)
x=tup.count(4)
print(x)

tup=(1,2,3,4,"dotcom","ส้ม",True,3.99)
x=tup.index(4)
print(x)

# การเรียงลำดับตัวเลข , ตัวอักษร
tup=(100.99,88,50,200,1,2,3,4,3.99,4)
tup.sort() #tuple ไม่มีฟังก์ชัน sort เหมือนกับ list
print(tup) # eror

tup=(100.99,88,50,200,1,2,3,4,3.99,4)
print("Before",tup)
lis=list(tup) # ต้องแปลง tup => lis ก่อน
lis.sort()
lis.reverse() # การย้อนกลับต้อง sort ก่อน ถึงจะ reverse ได้
tup=tuple(lis)
print("After=>",tup)

# การนำค่า tuple => ตัวแปร
tup=(10,20,30,)
a,b,c,=tup # กระจายสมาชิกไปใส่ในตัวแปรได้
print(a)
print(b)
print(c)
d=a+c
print(d)

# การสลับ tuple
x=(50,60)
y=(88,99)
print("Before x =>",x)
print("Before y =>",y)

x,y=y,x
print("After x =>",x)
print("After y =>",y)

# การแปลง tuple => string
charector=("d","o","t","c","o","m")
name="".join(charector)
print(name)

# reverse tuple
x=(100,20,30,15,10,5,500)
y=tuple(reversed(x)) # แปลงให้เป็น tuple
print(y)

x="dotcom"
y=tuple(reversed(x)) # แปลงให้เป็น tuple
print(y)