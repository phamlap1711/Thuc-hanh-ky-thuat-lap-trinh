print("Pham Tien lap")
print("248752021610071")
import numpy as np
# Tạo kiểu dữ liệu có cấu trúc
dt = np.dtype([
    ('name', 'U20'),      # Chuỗi Unicode tối đa 20 ký tự
    ('age', 'i1'),        # Số nguyên 1 byte
    ('score', 'f4')       # Số thực 4 byte
])
# Tạo mảng dữ liệu
sinhvien = np.array([
    ('An', 18, 7.5),
    ('Bình', 19, 8.2),
    ('Châu', 18, 6.9),
    ('Dũng', 20, 9.1),
    ('Hà', 19, 7.8)
], dtype=dt)
print("Dữ liệu ban đầu:")
print(sinhvien)
# Sắp xếp theo cột 'score'
sap_xep = np.sort(sinhvien, order='score')
print("\nDữ liệu sau khi sắp xếp theo điểm:")
print(sap_xep)
