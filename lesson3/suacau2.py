so_kwh = int(input("Nhập số kWh tiêu thụ: "))

tien_dien = so_kwh
if so_kwh < 0: print("tien dien phai la so nguyen duong")
if so_kwh <= 50: tien_dien = so_kwh * 1700
elif so_kwh > 50 and so_kwh <= 100: tien_dien (50 * 1700) + (so_kwh-50) * 1900
elif so_kwh <= 200: tien_dien = (50 * 1700) + (50*1900) + (so_kwh - 100) * 2100
else: tien_dien = (50*1700) + (50*1900) + (100*2100) + (so_kwh - 200) * 3000
print("Số tiền điện phải trả là:", tien_dien, "đồng")