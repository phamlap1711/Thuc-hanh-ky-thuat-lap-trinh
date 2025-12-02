print("Phạm Tiến Lập")
print("245752021610071")
s = input("Nhập chuỗi: ")
for ch in s:
    if ch == " " or ch == "\t":
        continue   # Bỏ qua không in ký tự này
    print(ch)
