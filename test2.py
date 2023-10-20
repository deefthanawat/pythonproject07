# character in string has index number
   # 01234567890123
infoA = 'Hello SAU 2023'
       # 43210987654321 คิอ = -

print(infoA[6]) #s #แสดงผลนับจากด้านหน้ากำหนด 1 ตำแหน่ง
print(infoA[-8]) #s #แสดงผลนับจากด้านหลัง 1 ตัว

# เข้าถึงตัวอักษรหลายๆ ตัวใน string เราจะใช้วิธี Sit<ing ด้วย index number
# SAU
print(infoA[6:9]) #นับจากด้านหน้ากำหนดตัวที่ 6 ถึง(:) 9 จะได้คำว่า SAU
print(infoA[-8:-5])

# 0 SAU 20
print(infoA[4:12])

# String Method คือ funtion ใช้งานด้วยตัว . 
print(infoA.upper())
print(infoA.lower())
print(infoA.capitalize())
print(infoA.title())
print(infoA.count('SAU'))
print(infoA.isdigit())
print(infoA.islower())
infoB = infoA.replace('SAU','IOS')
print(infoA)
print(infoB)
print(infoB.replace('Hello', 'RI...'))

# String function
print( len(infoA) )
 
print('SAU',35,end='') # SAU 35 
print('SAU'+str(35)) #SAU35 แปลงให้ตัวเลขเป็นช้อความ
print('SAU',35,sep='') #SAU35
print('20','02','2023',sep='/')
print(20,'มกราคม',2023,sep='/')








