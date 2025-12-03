print("Pham Tien Lap")
print("248752021610071")

import numpy as np

# ===================== DỮ LIỆU ĐẦU VÀO =====================
student_id = np.array([1011, 3012, 4231, 1011, 3097, 5211])
student_height = np.array([41.5, 42.3, 39.2, 41.5, 40.0, 43.1])

print("\n=== Dữ liệu gốc ===")
print("ID học sinh:", student_id)
print("Chiều cao :", student_height)

# ===================== SẮP XẾP THEO NHIỀU TIÊU CHÍ =====================
# Ưu tiên 1: ID tăng dần
# Ưu tiên 2: Chiều cao tăng dần khi ID trùng nhau

sort_index = np.lexsort((student_height, student_id))

sorted_id = student_id[sort_index]
sorted_height = student_height[sort_index]

# ===================== KẾT QUẢ =====================
print("\n=== Kết quả sắp xếp (ID ↑ , Height ↑) ===")
for i in range(len(sorted_id)):
    print(f"ID: {sorted_id[i]}  -  Height: {sorted_height[i]}")
