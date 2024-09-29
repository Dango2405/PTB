# Nhập xâu từ bàn phím
s = input("Nhập ngày tháng năm theo định dạng dd/mm/yyyy: ")

# Tách ngày, tháng, năm từ xâu
dd, mm, yyyy = s.split('/')

# In ra kết quả theo định dạng yêu cầu
print(f"Ngày {dd} tháng {mm} năm {yyyy}")
