# arr = [0,1,2,3,4,5,6]
# list_fruit = ["Apple","Banana","Lemon",]


# print(arr[3])
# print(list_fruit[2])







# print(len(arr))

# for i in range(len(arr)):
#     print(arr[i])


# for i in range(len(list_fruit)):
#     print(list_fruit[i])


# Khởi tạo mảng gồm 10 số
# arr = [15, 28, 30, 45, 50, 63, 75, 90, 102, 120]

# # Lọc và in các số chia hết cho cả 3 và 5
# print("Các số chia hết cho cả 3 và 5 là:")
# for i in range(len(arr)):
#         if arr[i] % 15 == 0:
#             print(arr[i])



# Khởi tạo mảng gồm 10 số
arr = [12, 7, 9, 14, 20, 33, 46, 55, 68, 81]

# Khởi tạo biến tổng
sum_of_even = 0

# Duyệt qua từng chỉ số trong mảng sử dụng range
for i in range(len(arr)):
    # Kiểm tra nếu số tại chỉ số i là số chẵn
    if arr[i] % 2 == 0:
        sum_of_even += arr[i]  # Cộng dồn số chẵn vào tổng

# In ra tổng của các số chẵn
print("Tổng các số chẵn trong mảng là:", sum_of_even)
