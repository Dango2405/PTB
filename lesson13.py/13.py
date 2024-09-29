# def absolute(n):
#     if n < 0:
#         return -n
#     else:
#         return n

# num = int(input("Enter a number: "))
# print("GIá trị tuyệt đối của", num, "là", absolute(num))

def is_odd(n):
    if n % 2 == 0:
        return False
    else:
        return True

print(is_odd(5))
print(is_odd(4))

