print("Phạm Tiến Lập")
print("245752021610071")
# a, b là 2 số Fibonacci đầu tiên
a, b = 1, 2
# Biến lưu tổng các số chẵn
total = 0
print(a, end=" ")
print(b, end=" ")
while a <= 4000000 - 1:
    if a % 2 == 0:
        total += a
    # Sinh số Fibonacci tiếp theo
    a, b = b, a + b
    print(a, end=" ")
print("\nTổng các số chẵn =", total)
