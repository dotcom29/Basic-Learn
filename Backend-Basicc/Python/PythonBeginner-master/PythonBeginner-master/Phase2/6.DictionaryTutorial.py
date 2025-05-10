# list , tuple
lis=["สีแดง","สีเหลือง","สีเขียว"]
tup=("สีแดง","สีเหลือง","สีเขียว")
#list , tuple => รับค่า flost ไม่ได้
#การเข้าถึงข้อมูลของ list,tuple คือการใช้ index

#การเข้าถึงข้อมูล dictionary => key (การเข้าถึงข้อมูล) : value (ค่าของข้อมูล)
# การสร้าง dict
colors={"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว","29":"วันเกิดคอม"}
city={"bangkok":"กรุงเทพ"}
animal={"ไก่":"chicken","แมว":"cat","dog":"น้องหมา"}
student={"ก้อง":"40","โจ้":"50","โค้ช":100}
room={300:"นาย A",301:"นาย B",302:"นาย C"}

print(colors["red"]) # ระบุ key ได้เลย
print(colors[29])
print(city["bangkok"])
print(animal["ก้อง"])
print(room[302])

# การระบุแบบ Constucktor
colors=dict({"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว","29":"วันเกิดคอม",True:"โสด"})
print(colors[29])
print(colors.get("red"))
print(colors[True])

# การเปลี่ยนข้อมูล
colors=dict({"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว","29":"วันเกิดคอม",True:"โสด"})
colors[29]="วันเกิดแอน"
print(colors)

# การเพิ่มข้อมูล
colors=dict({"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว","29":"วันเกิดคอม",True:"โสด"})
print(colors)
colors.update({"blue":"สีน้ำเงิน"}) # เพิ่มข้อมูลเดี่ยว
colors.update({"orange":"สีส้ม"})
colors.update({"orange":"สีส้ม","blue":"สีน้ำเงิน"}) # เพิ่มข้อมูลที่ละมากๆ
colors.update({"orange":"สีส้ม","blue":"สีน้ำเงิน","red":"สีชมพู"}) # การเพิ่มข้อมูลซ้ำ คือการแก้ไขข้อมูล
print(colors)

# การวนลูป
colors=dict({"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว"})
for item in colors:
    print(item) # key

for item in colors.keys:
    print(item) # key    

for item in colors.values:
    print(item) # Value

for item in colors.item():
    print(item) # key + Value

for k,v in colors.item(): # key + Value
    print(k)
    print(v)