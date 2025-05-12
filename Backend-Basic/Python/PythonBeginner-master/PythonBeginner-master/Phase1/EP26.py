# Loop ซ้อน Loop

# while ซ้อน while
i=1
while i<=3 :
    j=1 # ตัวนับ
    while j<=5: # พอ lopp ข้างในเป็นเท็จแล้ว(j>5) ก็จะไปทำงานที่ loop นอกต่อ
        print("รอบที่ = ",i," ตำแหน่งที่ = ", j)
        j+=1
    i+=1

# for ซ้อน for
for i in range(1,4):
    print("รอบที่ = ",i)
    for j in range(1,6):
        print("ตำแหน่งที่ = ", j)