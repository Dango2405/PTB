# Danh sách A
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Khởi tạo biến tổng cho các số chẵn
tong_chan = 0

# Duyệt qua từng số trong danh sách A
for i in A:
    # Kiểm tra xem số có phải là số chẵn không
    if i % 2 == 0:
        # Cộng số chẵn vào tổng
        tong_chan += i

# Xuất tổng các số chẵn
print("Tổng các số chẵn trong danh sách A là:", tong_chan)
