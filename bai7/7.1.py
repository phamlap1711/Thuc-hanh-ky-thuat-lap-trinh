print("Phạm Tiến Lập")
print("248752021610071")

# Mở file và đọc nội dung
file_path = input("Nhập vào tên file (ví dụ: C:/Users/Tran Van Viet/Documents/4.3.py): ")

try:
    with open(file_path, "r", encoding="utf-8") as input_file:
        for line in input_file:
            line = line.strip()          # Xóa \n, tab, khoảng trắng
            reversed_line = line[::-1]   # Đảo ngược dòng
            print(reversed_line)

except FileNotFoundError:
    print("Không tìm thấy file. Vui lòng kiểm tra lại đường dẫn!")
except Exception as e:
    print("Lỗi:", e)
