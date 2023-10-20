# ------- Tuple ข้อมูลหลายข้อมูล คนละฃนิด ซ้ำกันได้ และมีลำดับ แก้ไขไม่ได้ได้ด้วย -------
        #    0   1    2    3    4         5
my_tuple = (10, 20, True, 10, 'SAU', (20, 'IOT'))
        #    6   5   4     3    2          1 ค่าติดลบ

# การเข้าถึงข้อมูลใน list เพื่อเอาข้อมูลออกมาใช้ 
print(my_tuple[4]) # SAU
print(my_tuple[-2]) # SAU
print(my_tuple[5]) # [20, 'IOT]
print(my_tuple[-1]) # [20, 'iot']
print(my_tuple[5][1])
print(my_tuple[-1][-1]) # IoT

# การเช้าถึงทีละหลายข้อมูล เราเรียกการ Slicing ผลลัพธ์จะเป็น tuple 
print(my_tuple[1:4])
print(my_tuple[3:])
print(my_tuple[:3])

# เข้าถึงทุกข้อมูล
for info in my_tuple :
    print (info, end=',')

print()

#  หากอยากจะแก้ข้อมูลใน tuple ทำได้ด้วยวิธีเฉพาะทาง
my_tuple = list ( my_tuple )
my_tuple[4] = 'IoT'
my_tuple = tuple(  )
print(my_tuple)

# tuple method 
print( my_tuple.count(10))
print( my_tuple.index('IoT'))

# Tuple Function
my_tuple3 = (10, 20, 10, 30, True)
print(len(my_tuple3))
print(min(my_tuple3))
print(max(my_tuple3))