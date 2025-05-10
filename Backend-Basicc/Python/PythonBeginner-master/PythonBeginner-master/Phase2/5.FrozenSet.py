# FrozenSet ไม่สามารถแก้ไขข้อมูลอะไรได้เลย
fruit=frozenset(["มะม่วง","มะยม","มะนาว"])
fruit.add("ทุเรียน")
fruit.discard("มะยม")
print(fruit) #eror
for item in fruit:
    print("ข้อมูล=>",item) #ปริ้นข้อมูลปต่ละตัว