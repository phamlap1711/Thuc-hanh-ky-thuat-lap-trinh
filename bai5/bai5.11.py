import numpy as np

# Dữ liệu sinh viên: (Tên, Lớp, Chiều cao)
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]

# Định nghĩa kiểu dữ liệu cấu trúc: tên (string), lớp (int), chiều cao (float)
dtype = [('name', 'U20'), ('class', int), ('height', float)]

# Tạo mảng cấu trúc
students = np.array(students_details, dtype=dtype)

print("Mảng ban đầu:")
print(students)

# Sắp xếp theo lớp, sau đó chiều cao
sorted_students = np.sort(students, order=['class', 'height'])

print("\nMảng sau khi sắp xếp (theo lớp, rồi chiều cao):")
print(sorted_students)
