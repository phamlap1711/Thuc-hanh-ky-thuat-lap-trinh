print("Phạm Tiến Lập")
print("245752021610071")
import re
value = []
items = [x for x in input("Nhập mật khẩu: ").split(',')]   # nhập nhiều mật khẩu, cách nhau bởi dấu ,
for p in items:
    # Kiểm tra độ dài
    if len(p) < 6 or len(p) > 12:
        continue
    # Kiểm tra các điều kiện của mật khẩu
    if not re.search("[a-z]", p):
        continue
    el
