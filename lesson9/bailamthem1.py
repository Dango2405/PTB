# Danh sách sản phẩm của cửa hàng
san_pham = {
    1: {"ten": "Sữa tươi", "gia": 30_000},
    2: {"ten": "Bánh mì", "gia": 15_000},
    3: {"ten": "Trái cây", "gia": 25_000},
    4: {"ten": "Rau củ", "gia": 20_000},
    5: {"ten": "Nước giải khát", "gia": 18_000},
    6: {"ten": "Thịt gà", "gia": 50_000},
    7: {"ten": "Cá hồi", "gia": 80_000},
    8: {"ten": "Phô mai", "gia": 40_000},
    9: {"ten": "Kem", "gia": 10_000}
}

# Giỏ hàng của người dùng
gio_hang = {}

# Hiển thị danh sách sản phẩm
def hien_thi_danh_sach_san_pham():
    print("==== DANH SÁCH SẢN PHẨM ====")
    for ma_sp, thong_tin in san_pham.items():
        print(f"{ma_sp}. {thong_tin['ten']} - {thong_tin['gia']} VNĐ")
    print("===========================")

# Thêm sản phẩm vào giỏ hàng
def them_san_pham_vao_gio_hang(ma_sp, so_luong):
    if ma_sp in san_pham:
        if ma_sp in gio_hang:
            gio_hang[ma_sp] += so_luong
        else:
            gio_hang[ma_sp] = so_luong
        print(f"Đã thêm {so_luong} {san_pham[ma_sp]['ten']} vào giỏ hàng.")
    else:
        print("Mã sản phẩm không hợp lệ.")

# Hiển thị giỏ hàng
def hien_thi_gio_hang():
    print("==== GIỎ HÀNG ====")
    tong_tien = 0
    for ma_sp, so_luong in gio_hang.items():
        ten_sp = san_pham[ma_sp]['ten']
        gia_sp = san_pham[ma_sp]['gia']
        tong_tien += gia_sp * so_luong
        print(f"{ten_sp} x {so_luong} - {gia_sp * so_luong} VNĐ")
    print(f"Tổng cộng: {tong_tien} VNĐ")
    print("=================")

# Thanh toán
def thanh_toan():
    if gio_hang:
        hien_thi_gio_hang()
        print("Cảm ơn bạn đã mua sắm tại cửa hàng của chúng tôi. Hẹn gặp lại!")
        gio_hang.clear()
    else:
        print("Giỏ hàng của bạn trống.")

# Chương trình chính
while True:
    print("\n=== ỨNG DỤNG CỬA HÀNG ===")
    print("1. Xem danh sách sản phẩm")
    print("2. Thêm sản phẩm vào giỏ hàng")
    print("3. Xem giỏ hàng")
    print("4. Thanh toán")
    print("5. Thoát")

    lua_chon = input("Chọn tùy chọn (1-5): ")

    if lua_chon == '1':
        hien_thi_danh_sach_san_pham()
    elif lua_chon == '2':
        ma_sp = int(input("Nhập mã sản phẩm: "))
        so_luong = int(input("Nhập số lượng: "))
        them_san_pham_vao_gio_hang(ma_sp, so_luong)
    elif lua_chon == '3':
        hien_thi_gio_hang()
    elif lua_chon == '4':
        thanh_toan()
    elif lua_chon == '5':
        print("Cảm ơn bạn đã sử dụng ứng dụng. Hẹn gặp lại!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
