print("Pham Tien Lap")
print("248752021610071")

from sorting_algorithms import bubbleSort

# Hàm nhập dữ liệu từ người dùng
def input_list():
    while True:
        try:
            n = int(input("Nhập số lượng phần tử: "))

            if n <= 0:
                print("Số lượng phải là số nguyên dương. Vui lòng nhập lại.")
                continue

            input_str = input(f"Nhập {n} số nguyên, cách nhau bằng khoảng trắng: ")
            lst = input_str.split()

            if len(lst) != n:
                print("Số lượng phần tử không khớp. Vui lòng nhập đúng số lượng!")
                continue

            # Chuyển tất cả phần tử sang kiểu số nguyên
            lst = [int(x) for x in lst]
            return lst

        except ValueError:
            print("Lỗi! Vui lòng chỉ nhập số nguyên.")

# ================= MAIN ================
if __name__ == "__main__":

    my_list = input_list()
    print("\nDanh sách ban đầu:", my_list)

    bubbleSort(my_list)

    print("\nDanh sách sau khi sắp xếp (Bubble Sort):", my_list)
