# Nhập các phần tử vào mảng
n = int(input("Nhập số lượng phần tử: "))
arr = []
for i in range(n):
    arr.append(int(input("Nhập phần tử thứ " + str(i+1) + ": ")))

# In các phần tử trong mảng
print("Các phần tử trong mảng là:")
for i in range(n):
    print(arr[i])
