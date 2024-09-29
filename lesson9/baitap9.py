# Bước 1: Nhập số lượng bài kiểm tra và điểm số
n = int(input("Nhập số lượng bài kiểm tra: "))
if n <= 0:
    print("Số lượng bài kiểm tra phải là số nguyên dương.")
else:
    diem_so = []
    for i in range(n):
        diem = int(input(f"Nhập điểm bài kiểm tra thứ {i+1}: "))
        diem_so.append(diem)
    
    # Bước 2: Sắp xếp danh sách điểm số theo chiều tăng dần
    diem_so.sort()
    
    # Bước 3: Xoá số điểm nhỏ nhất (Nếu có hai số điểm nhỏ nhất thì xoá cả hai)
    if diem_so:
        min_diem = diem_so[0]
        diem_so = [diem for diem in diem_so if diem != min_diem]
    
    # Bước 4: Xuất danh sách điểm sau khi đã xử lý yêu cầu 1 và 2
    print("Danh sách điểm sau khi xử lý:")
    print(diem_so)
    
    # Đếm số lượng điểm lớn hơn hoặc bằng 8
    dem = 0
    for diem in diem_so:
        if diem >= 8:
            dem += 1
            
    print("Số lượng điểm lớn hơn hoặc bằng 8:", dem)
