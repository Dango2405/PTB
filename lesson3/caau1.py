loai_giay_1 = 1
so_trang_1 = 13
loai_giay_2 = 2
so_trang_2 = 10

so_giay1 = 0
so_giay2 = 0

if loai_giay_1 == 1:
    so_giay1 = so_trang_1
else:
    so_giay1 = (so_trang_1 + 1) // 2

if loai_giay_2 == 1:
    so_giay2 = so_trang_2
else:
    so_giay2 = (so_trang_2 + 1) // 2

# In kết quả
print("loại giấy tờ", loai_giay_1, "số trang", so_trang_1, "số lượng giấy cần dùng:", so_giay1)
print("loại giấy tờ", loai_giay_2, "số trang", so_trang_2, "số lượng giấy cần dùng:", so_giay2)