print("Pham Tien Lap")
print("248752021610071")

import numpy as np

data = [
    ("Nam", 5, 40.5),
    ("Linh", 6, 42.0),
    ("An", 5, 39.8),
    ("Hoài", 7, 44.1),
    ("Paul", 6, 42.3)
]

# Kiểu dữ liệu cho mảng có cấu trúc
data_type = [('name', 'U20'), ('class', 'i4'), ('height', 'f4')]

# Tạo mảng structured array
students = np.array(data, dtype=data_type)

print("\n=== Mảng Gốc (Chưa sắp xếp) ===")
print(students)

# Sắp xếp theo nhiều tiêu chí: class tăng dần → height tăng dần
sort_fields = ['class', 'height']

sorted_students = np.sort(students, order=sort_fields)

print("\n=== Kết Quả Sắp Xếp (Lớp tăng dần, Chiều cao tăng dần) ===")
print(sorted_students)
