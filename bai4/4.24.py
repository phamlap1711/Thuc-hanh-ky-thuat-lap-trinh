print("Phạm Tiến Lập")
print("2455752021610071")
s = input("Nhập một câu: ")
# Khởi tạo biến đếm
dem_hoa = 0
dem_thuong = 0
# Duyệt qua từng ký tự trong chuỗi
for ch in s:
    if ch.isupper():        # Nếu là chữ hoa (A-Z)
        dem_hoa += 1
    elif ch.islower():      # Nếu là chữ thường (a-z)
        dem_thuong += 1
print("Số chữ hoa:", dem_hoa)
print("Số chữ thường:", dem_thuong)
