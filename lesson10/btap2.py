 # Nhập số tiền chi tiêu mỗi ngày
chi_tieu = []
for i in range(6):
    so_tien = float(input(f"Nhập số tiền chi tiêu ngày thứ {i+2}: "))
    chi_tieu.append(so_tien)

  # Tính tổng chi tiêu
tong_chi_tieu = 0
for so_tien in chi_tieu:
    tong_chi_tieu += so_tien

  # Tìm ngày chi tiêu nhiều nhất
ngay_nhieu_nhat = 0  
so_tien_nhieu_nhat = chi_tieu[0]
for i in range(1, len(chi_tieu)):
    if chi_tieu[i] > so_tien_nhieu_nhat:
      so_tien_nhieu_nhat = chi_tieu[i]
      ngay_nhieu_nhat = i + 2

  # Tính trung bình chi tiêu mỗi ngày
trung_binh = tong_chi_tieu / 6

  # In kết quả
print("Tổng số tiền chi tiêu trong tuần:", tong_chi_tieu)
print("Ngày chi tiêu nhiều nhất là ngày thứ", ngay_nhieu_nhat)
print("Trung bình mỗi ngày chi tiêu:", trung_binh)
