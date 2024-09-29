def tinh_diem_trung_binh(diem_so):
    tong = 0
    for diem in diem_so:
        tong = tong + diem
    tong = tong + diem_so[-1]  # Cộng thêm điểm cuối cùng một lần nữa
    
    so_diem = len(diem_so) + 1
    diem_trung_binh = tong / so_diem
    return round(diem_trung_binh, 1)

# Sử dụng hàm
diem_tin_hoc = [9, 6, 10, 7]
ket_qua = tinh_diem_trung_binh(diem_tin_hoc)

print("Danh sách điểm số:")
for diem in diem_tin_hoc:
    print(diem)

print("Điểm trung bình:", ket_qua)