# Xác định mật khẩu cho trước
password = "Quocbao24052011"

# Lặp để yêu cầu nhập mật khẩu và kiểm tra
while True:
    # Nhập mật khẩu từ người dùng
    entered_password = input("Nhập mật khẩu: ")
    
    # Kiểm tra mật khẩu
    if entered_password == password:
        print("Đăng nhập thành công")
        break  # Thoát khỏi vòng lặp nếu mật khẩu đúng
    else:
        print("Mật khẩu không chính xác. Vui lòng thử lại.")
