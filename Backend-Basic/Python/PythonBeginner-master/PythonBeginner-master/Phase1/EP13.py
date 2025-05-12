# Assignment1
# โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง (m)
# input / convert to integer

# วิธีแรก
weight=int(input("ป้อนน้ำหนักของคุณ (kg):"))
high=int(input("ป้อนส่วนสูงของคุณ (cm) :"))

#process
#cm => m
high/=100

#calculate bmi
bmi=weight/(high*high)

#output
print("BMI = ",bmi)



# วิธีสอง
weight=int(input("ป้อนน้ำหนักของคุณ (kg):"))
high=int(input("ป้อนส่วนสูงของคุณ (cm) :"))/100
print("BMI = ",weight/(high**2))