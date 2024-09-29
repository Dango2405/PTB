# Nhập số kWh điện tiêu thụ từ người dùng
kWh = int(input("Nhập số kWh điện tiêu thụ trong tháng: "))

# Biến để tính tổng số tiền điện
total_money = 0

# Xử lý từng khoảng số kWh và tính toán số tiền điện tương ứng
if kWh <= 50:
    gia_dien = 1700  # Đơn giá 1.700 đồng/kWh
    total_money = kWh * gia_dien
    print("Số tiền điện cần phải trả:", total_money, "đồng")
else:
    # Tính tiền cho 50 kWh đầu tiên
    total_money += 50 * 1700
    print("- 50 kWh đầu tiên sẽ được tính với giá 1.700 đồng/kWh, tương ứng với", 50 * 1700, "đồng.")

if kWh > 50 and kWh <= 100:
    gia_dien = 1900  # Đơn giá 1.900 đồng/kWh