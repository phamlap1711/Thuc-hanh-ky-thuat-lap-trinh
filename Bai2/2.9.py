print("Phạm Tiến Lập")
print("245752021610071")
# Nhập vào một chuỗi
s = input("Nhập string: ")
# Tạo một dictionary rỗng
d = {}
# Đếm số lần xuất hiện của từng ký tự
for i in s:
    d[i] = s.count(i)
print(d)
