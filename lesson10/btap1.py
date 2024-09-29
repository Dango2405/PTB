# Khởi tạo danh sách
A = [5, 12, 15, 7, 7, 30, 3, 56]

# Khởi tạo biến để lưu tổng của các số chẵn
total = 0

# Duyệt qua từng phần tử của danh sách
for i in A:
    # Kiểm tra nếu phần tử là số chẵn
    if i % 2 == 0:
        # Cộng số chẵn vào tổng
        total += i

# In tổng của các số chẵn
print(total)
