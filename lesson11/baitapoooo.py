
# full_name = input("Nhập họ và tên: ")


# first_name = full_name.split()[0]



# print(first_name)

s = input("Nhập vào một xâu ngày tháng (dd/mm/yyyy): ")
result = "Ngày" + s
# Thay thế '/' đầu bằng ' tháng ww ~
result = result.replace('/', 'tháng', 1)
# Thay thế '/' cuối cùng bằng năm 1
result = result.replace('/', 'năm ')
print(result)