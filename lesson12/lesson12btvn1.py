def hien_thi_xau_tang_dan(xau):
    for i in range(len(xau)):
        print(xau[:i+1])

# Sử dụng hàm
xau_nhap = input("Nhập xâu ký tự: ")
hien_thi_xau_tang_dan(xau_nhap)