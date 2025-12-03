print("Phạm Tién Lập")
print("245752021610071")

import shutil
import os

def copy_file_shutil(source_path, destination_path):
    try:
        shutil.copyfile(source_path, destination_path)
        print(f"Sao chép thành công (shutil) từ '{source_path}' sang '{destination_path}'!")
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tệp nguồn tại đường dẫn '{source_path}'!")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
copy_file_shutil(r"C:/Users/Tran Van Viet/Documents/6.6.py",
                 r"C:/Users/Tran Van Viet/Documents/6.6_copy.py")

