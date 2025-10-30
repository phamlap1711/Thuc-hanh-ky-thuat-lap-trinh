import numpy as np
students = np.array([
    (101, 170.5),
    (102, 165.2),
    (103, 172.0),
    (104, 168.3)
])
ids = students[:, 0]
heights = students[:, 1]
sorted_indices = np.lexsort((ids, heights))
sorted_students = students[sorted_indices]
print("Chỉ số sắp xếp:", sorted_indices)
print("Dữ liệu đã sắp xếp (theo chiều cao tăng dần):")
print(sorted_students)
