# Nhập danh sách điểm số từ bàn phím
s = input("Nhập danh sách điểm số, mỗi điểm cách nhau bởi một khoảng trắng: ")

# Tách các điểm số thành một danh sách
diem_so = s.split()

# Đếm số lượng điểm 10
so_luong_diem_10 = diem_so.count('10')

# Kiểm tra và in ra kết quả
if so_luong_diem_10 > 0:
    print(f"Số lượng điểm 10: {so_luong_diem_10}")
else:
    print("Bạn chưa có điểm 10")
