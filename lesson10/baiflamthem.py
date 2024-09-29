# Khởi tạo danh sách sản phẩm
san_pham = [
    "Sữa tươi",
    "Bánh mì",
    "Trái cây",
    "Rau củ",
    "Nước giải khát",
    "Thịt gà",
    "Cá hồi",
    "Phô mai",
    "Kem"
]

# Hiển thị menu
print("==== MENU SẢN PHẨM ====")
for i, sp in enumerate(san_pham, 1):
    print(f"{i}. {sp}")
print("=======================")

# Yêu cầu người dùng chọn sản phẩm
while True:
    lua_chon = input("Chọn số sản phẩm để xem chi tiết (0 để thoát): ")
    
    # Kiểm tra nếu người dùng muốn thoát
    if lua_chon == '0':
        print("Cảm ơn bạn đã sử dụng dịch vụ. Hẹn gặp lại!")
        break
    
    # Kiểm tra nếu người dùng nhập số
    if lua_chon.isdigit():
        lua_chon = int(lua_chon)
        # Kiểm tra nếu số chọn hợp lệ
        if 1 <= lua_chon <= len(san_pham):
            print(f"Chi tiết sản phẩm: {san_pham[lua_chon - 1]}")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
    else:
        print("Vui lòng nhập một số hợp lệ.")
