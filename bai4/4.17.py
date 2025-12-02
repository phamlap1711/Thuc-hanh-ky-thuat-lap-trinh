print("Phạm Tiến Lập")
print("2455752021610071")
try:
    n_str = input("Nhập số nguyên n: ")
    n = int(n_str)
except ValueError:
    print("Vui lòng nhập số nguyên.")
    exit()
if n < 1:
    print("Hãy nhập số nguyên dương.")
else:
    for i in range(1, n):
        print(i)
