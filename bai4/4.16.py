print("Phạm Tiến Lập")
print("2455752021610071")
so_nhi_phan = input("Nhập số nhị phân nối nhau bằng dấu phẩy: ")
# split(',') sẽ tách chuỗi thành các phần tử khi gặp dấu ','
chuoi_so_nhi_phan = so_nhi_phan.split(',')
for ch in chuoi_so_nhi_phan:
    print(ch)
