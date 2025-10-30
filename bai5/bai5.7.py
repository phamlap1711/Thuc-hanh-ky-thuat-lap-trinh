import numpy as np
data_type = [('name', 'U20'),  
             ('height', float),
             ('class', int)]    
students_details = [
    ('An', 1.72, 10),
    ('Bình', 1.65, 11),
    ('Chi', 1.80, 12),
    ('Dũng', 1.60, 10),
    ('Hà', 1.75, 11)
    ]
student_array = np.array(students_details, dtype=data_type)
print("Mảng ban đầu:")
print(student_array)
sorted_array = np.sort(student_array, order='height')
print("\nMảng sau khi sắp xếp theo chiều cao:")
print(sorted_array)
