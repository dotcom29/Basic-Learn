x = 10
y = 3.14
z = "20"

print(type(x))
print(type(y))
print(type(z))

# int + int
result = x+y # 10+3.14 = 13.14
print(result)

# แปลง str => int (ไม่ถาวร เพราะแปลงชนิดข้อมูลแค่บรรทัดนี้เท่านั้น)
ผลลัพธ์ = x+int(z) # "20" + 10 = 30
print(ผลลัพธ์)

# แปลง int => str
แปรผล = str(x)+z # "10" + "20" = 1020
print(แปรผล)

# แปลง str => float
print(float(z))

# แปลง float => str
print(str(y))

# แปลง float => int
print(int(y))


#วิธีเปลี่ยนชนิดข้อมูลแบบถาวร
A = 10 # A เป็น int
#จะเปลี่ยน A ให้เป็น flost ถาวร
A = float(A)
print(type(A))