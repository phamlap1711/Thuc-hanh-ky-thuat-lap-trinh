print("Phạm Tiến Lập")
print("245752021610071")

def lay_n_dong_cuoi_cung(ten_tep, n):
    with open(ten_tep, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    return lines[-n:]

danh_sach_dong = lay_n_dong_cuoi_cung(r'C:/Users/Tran Van Viet/Documents/5.10.py', 3)
for line in danh_sach_dong:
    print(line, end="")
