# BMI = น้ำหนัก(kg) / ส่วนสูง(m)

#input
weight = int(input("กรุณาป้อนน้ำหนักของคุณ (kg) :")) #convert to integer
high = int(input("กรุณาป้อนส่วนสูงของคุณ (cm) :")) #convert to integer

#process
high = high/100 #แปลงจาก cm => m  #ฉบับย่อ high/=100
bmi = weight/(high*high) #calculate

 
#output
print("BMI = " , bmi)

#วิธีที่2 แบบยุบราม
#weight = int(input("กรุณาป้อนน้ำหนักของคุณ (kg) :"))
#high = int(input("กรุณาป้อนส่วนสูงของคุณ (cm) :"))/100
#print("bmi = ",weight/high**2)

