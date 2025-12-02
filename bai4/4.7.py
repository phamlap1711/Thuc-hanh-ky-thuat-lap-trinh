print("Phạm Tiến Lập")
print("245752021610071")   # Nếu bạn muốn giữ dòng này
ho_va_ten = "Phạm Tiến Lập"   # thay cho input
# rsplit: tách từ phải sang trái, chỉ tách 1 lần
chu_cai = ho_va_ten.rsplit(' ', 1)
ho_va_ten_dem = chu_cai[0]   # Họ và tên đệm
ten = chu_cai[1]             # Tên riêng
print("Họ và Tên đệm:", ho_va_ten_dem)
print("Tên riêng:", ten)
