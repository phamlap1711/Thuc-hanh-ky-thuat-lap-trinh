print("Phạm Tiến Lập")
print("245752021610071")
chuoi_goc = input("Nhập chuỗi: ")
chuoi_moi = ""
for kytu in chuoi_goc:
    if kytu.isdigit():   # Nếu là số thì bỏ qua
        continue
    else:
        chuoi_moi += kytu
print("Chuỗi sau khi loại bỏ số:", chuoi_moi)
