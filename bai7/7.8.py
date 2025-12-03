print("Phạm Tiến Lập")
print("245752021610071")
danh_sach_moi = ['Dưa hấu', 'Nho', 'Chuối']
with open('thfd.py', 'a', encoding='utf-8') as f:
    for i in danh_sach_moi:
        f.write(i + '\n')
print("Đã thêm danh sách mới vào cuối tệp!")
