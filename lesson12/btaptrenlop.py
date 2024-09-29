def rut_gon_phan_so(tu, mau):
    def ucln(a, b):
        a,b = max(a,-a), max(b,-b)
        while b:
            a, b = b, a % b
        return a
    
    uoc_chung = ucln(tu,mau)
    return tu // uoc_chung, mau // uoc_chung

def tinh_tong_phan_so(tu1, mau1, tu2, mau2):
    tu = tu1 * mau2 + tu2 * mau1
    mau = mau1 * mau2
    return rut_gon_phan_so(tu, mau)

# Nhập dữ liệu
tu1 = int(input("Nhập tử số của phân số thứ nhất: "))
mau1 = int(input("Nhập mẫu số của phân số thứ nhất: "))
tu2 = int(input("Nhập tử số của phân số thứ hai: "))
mau2 = int(input("Nhập mẫu số của phân số thứ hai: "))

# Tính tổng và rút gọn
tong_tu, tong_mau = tinh_tong_phan_so(tu1, mau1, tu2, mau2)

# Xuất kết quả
print(f"Tổng của hai phân số là:{tong_tu}/{tong_mau}")
