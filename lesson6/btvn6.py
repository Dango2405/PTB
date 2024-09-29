# Nhập số nguyên dương n từ người dùng
n = int(input("Nhập một số nguyên dương n: "))

# Khởi tạo biến s để lưu trữ tổng
s = 0

# Tính tổng các số từ 1 đến n bằng vòng lặp for
for i in range(1, n + 1):
    s += i  # Cộng giá trị của i vào s

# In kết quả ra màn hình
print("Tổng các số từ 1 đến", n, "là:", s)
