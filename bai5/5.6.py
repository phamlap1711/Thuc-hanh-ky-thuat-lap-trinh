print("Phạm Tiến Lập")
print("248752021610071")
lst = input("Nhập các giá trị của list: ")
in_lst = [int(a) for a in lst.split()]
print("Max list là:", max(in_lst))
print("Min list là:", min(in_lst))
print("Vị trí của phần tử lớn nhất là:", in_lst.index(max(in_lst)))
print("Vị trí của phần tử nhỏ nhất là:", in_lst.index(min(in_lst)))
