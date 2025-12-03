print("Phạm Tiến Lập")
print("245752021610071")

import mymath   # Module phải có file mymath.py

values = [2, 4, 6, 8, 10]

print('Squares:')
for v in values:
    print(mymath.squares(v))   # Gọi hàm squares trong mymath

print('Cubes:')
for v in values:
    print(mymath.cubes(v))     # Sửa lỗi "myath" → mymath

print('Average: ' + str(mymath.average(values)))
