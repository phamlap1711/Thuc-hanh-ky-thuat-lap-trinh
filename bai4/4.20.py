print("Phạm Tiến Lập")
print("2455752021610071")
# In ra n dòng đầu tiên của tam giác Pascal
n = int(input("Nhập số dòng n: "))
for i in range(n):
    # Khởi tạo phần tử đầu tiên của hàng là 1
    num = 1
    # In khoảng trắng để tạo hình tam giác Pascal
    print(" " * (n - i), end="")
    # In các giá trị trong hàng
    for j in range(i + 1):
        print(num, end=" ")
        # Tính giá trị tiếp theo trong hàng
        num = num * (i - j) // (j + 1)
    print()
