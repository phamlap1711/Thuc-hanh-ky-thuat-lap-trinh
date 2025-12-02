print("Phạm Tiến Lập")
print("245752026160071")
danhsach = input("Nhập chuỗi: ").split()
# Xóa phần tử 'xyz' nếu nó tồn tại trong danh sách
if "xyz" in danhsach:
    danhsach.remove("xyz")
for c in danhsach:
    print(c)
