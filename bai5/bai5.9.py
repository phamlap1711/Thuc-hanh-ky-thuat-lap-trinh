def binary_search(lst, value):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if lst[mid] == value:
            return True
        elif lst[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return False
n = int(input("Nhập số lượng phần tử của danh sách: "))
lst = list(map(int, input(f"Nhập {n} số, cách nhau bởi dấu cách: ").split()))
while len(lst) != n:
    print(f"Số lượng nhập không đúng, hãy nhập lại {n} số:")
    lst = list(map(int, input().split()))
lst.sort()
value = int(input("Nhập phần tử cần tìm: "))
found = binary_search(lst, value)
print(f"Danh sách đã sắp xếp: {lst}")
print(f"Phần tử {value} {'có' if found else 'không có'} trong danh sách.")
