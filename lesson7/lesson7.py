# i    =    1
# while i<10:
#      print(i)
#      i = i+1



# for i in range(True):
#     print(i)


# while True:
#     n = int(input("Nhập số nguyên n: "))
#     if n <= 0:
#         continue
#     for i in range(n, 101):
#         print(i)
#     break
    

import random

number_computer = random.randint(1,20)

count = 0
while True:
    num = int(input("Nhập số bạn đoán:"))
    count += 1

    if num < number_computer:
        print("Số của bạn đoán nhỏ hơn")
    elif num > number_computer:
        print("Số của bạn đoán lớn hơn")
    else:
        print("Mày đã đoán đúng !!!.Số lần đoán là:" , count)
        break
        
