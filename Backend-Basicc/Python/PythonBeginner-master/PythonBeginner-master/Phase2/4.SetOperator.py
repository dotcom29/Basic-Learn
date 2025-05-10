#union , การรวม
fruitA={"กล้วย","มะยม","มะนาว"}
fruitB={"สตอ","กีวี","มะม่วง"}
fruitA.update(fruitB) # การรวมแบบที่ 1 , เพิ่มโดยไม่เปลืองหน่วยความจำ
allfruit=fruitA.union(fruitB) # การรวม 2
fruitC=fruitA.copy() #ื การคัดลอก
print(fruitA)
print(allfruit)
print(fruitC)

#difference , การแสดงสมาชิกที่ไม่เหมือนกัน
fruitA={"กล้วย","มะยม","มะนาว","แอปเปิ้ล","ทุเรียน"}
fruitB={"แอปเปิ้ล","ทุเรียน","สตอ","กีวี","มะม่วง"}
fruitC=fruitA.difference(fruitB)
fruitA.difference_update(fruitB) #การเพิ่มข้อมูลที่แตกต่างลงใน fruitA , ไม่ต้องสร้างตัวแปรใหม่
print(fruitC)

#intersection , การแสดงสมาชิกที่เหมือนกัน
fruitA={"กล้วย","มะยม","มะนาว","แอปเปิ้ล","ทุเรียน"}
fruitB={"แอปเปิ้ล","ทุเรียน","สตอ","กีวี","มะม่วง"}
fruitC=fruitA.intersection(fruitB)
fruitA.intersection_update(fruitB) #การเก็บข้อมูลเฉพาะที่เหมือนกันลงใน fruitA

#subset เช่น ประเทศไทย - เชียงใหม่(subset)
#superset
fish={"ปลาดุก","ปลาหมอ","ปลาวาฬ","ปลาโลมา","ปลาฉลาม","ปลาตะเพียน"}
#subset
x={"ปลาดุก","ปลาฉลาม"}
y={"ปลาวาฬ","ปลาฉลาม"}
#การเช็คsubset
print(x.issubset(fish))
print(fish.issuperset(x))

# min , max
number={3,4,5,100,80,900,1000,500,300,-100,-8,-150}
print(min(number))
print(max(number))