print("Phạm Tiến Lập")
print("248752021610071")

# Nhập tên file
file_name = input("Nhập vào tên file (Ví dụ:C:/Users/Tran Van Viet/Documents/6.1.py): ")

try:
    with open(file_name, "r", encoding="utf-8") as input_file:
        doc_file = input_file.read()

        # Đếm ký tự
        tong_ky_tu = len(doc_file)

        # Đếm số từ
        tong_tu = len(doc_file.split())

        # Đếm số dòng
        tong_dong = len(doc_file.splitlines())

    print("\n----- Kết quả thống kê file -----")
    print("Tên file:", file_name)
    print("Số ký tự:", tong_ky_tu)
    print("Số từ:", tong_tu)
    print("Số dòng:", tong_dong)

except FileNotFoundError:
    print("Không tìm thấy file. Vui lòng kiểm tra lại đường dẫn!")
except Exception as e:
    print("Lỗi:", e)
