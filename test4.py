# ----- list คือ ข้อมูลหลายข้อมูล คนละขนิด ซ้ำกันได้ และมีลำดับ อีกทั้งยังแก้ไขได้ด้วย -----

my_list = [10 , 
           20 , 
           True, 
           10 , 
           'SAU' , 
           [20 , 'IoT']]

# การเข้าถึงข้อมูลใน list เพื่อเอาข้อมูลออกมาใช้ หรือแก้ไขค่าข้อมูลให้มันใหม่
# เข้าถึงข้อมูล
print(my_list[4]) # SAU
print(my_list[-2]) # SAU
print(my_list[5]) # [20, 'IOT]
print(my_list[-1]) # [20, 'iot']
print(my_list[-1][-1]) # IoT


# เข้าถึงทีละหลายข้อมูล เราเรียกการ Slicing ผลลัพธ์จะเป็น list
print( my_list[1:4] ) # 20, true, 10
print( my_list[3:]) # 10, 'sau', [20, 'iot'] 
print( my_list[:3] ) # แสดงผลก่อนหน้า 3 ทั้งหมด

# เข้าถึงทุกข้อมูล
for info in my_list : 
    print(info, end=',')

print ()

print(my_list)
my_list[4] = 'Thailand'
print(my_list)

# List Method
my_list2 =[10, 20, True , 10 , 'SUA' , [20 , 'IOT']]
my_list2.append( 'WOW' )
print(my_list2)
my_list2.append([111,111,333])
print(my_list2)
my_list2.extend([444,555])
print(my_list2)
my_list2.remove(10)
my_list2.remove( 'SAU' )
my_list2.remove([111,111,333])
print(my_list2)
my_list2.pop()
my_list2.pop()
my_list2.pop()
print(my_list2)
my_list2.pop(2) # 2 คือ index
print(my_list2)

# List Function -> len() , min() , max()
my_list3 = [10,20,10,30,True]
print(len(my_list3))
print(min(my_list3))
print(max(my_list3))
