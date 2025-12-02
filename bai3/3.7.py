print("Phạm Tiến Lập")
print("245752021610071")
print("Nhập các lệnh di chuyển của robot. Gộm Up (U), Down (D), Left (L), Right (R)")
print("Mỗi lệnh nhập cách nhau bằng dấu cách")
x = 0
y = 0
# Nhập lặp đến khi đúng
while True:
    data = input("Nhập lệnh: ")
    arr = data.split()
    # Kiểm tra rỗng
    if len(arr) == 0:
        print("Không được để trống, nhập lại!")
        continue
    # Kiểm tra hợp lệ
    hop_le = True
    for i in arr:
        if i not in ["U", "D", "L", "R"]:
            hop_le = False
            break
    if hop_le:
        break
    else:
        print("Có ký tự không hợp lệ! Chỉ nhập U/D/L/R, nhập lại!")

# Xử lý từng lệnh
for i in arr:
    if i == "U":
        y += 1
    elif i == "D":
        y -= 1
    elif i == "L":
        x -= 1
    elif i == "R":
        x += 1
# Tính khoảng cách
kc = (x**2 + y**2) ** 0.5
print("Tọa độ cuối cùng của robot là: (", x, ",", y, ")")
print("Khoảng cách robot di chuyển từ vị trí ban đầu là:", kc)
