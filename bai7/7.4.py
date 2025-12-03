print("Phạm Tiến Lập")
print("245752021610071")

def file_read_from_head(tên_file, so_dong):
    from itertools import islice
    with open(tên_file, encoding='utf-8') as f:
        for line in islice(f, so_dong):
            # islice yêu cầu file trả về dòng nào đó rồi dừng lại
            # và không đọc thêm dòng khác
            print(line)

file_read_from_head(r'C:/Users/Tran Van Viet/Documents/5.5.py', 2)
