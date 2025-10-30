def bubbleSort(nlist):
    """
    Sắp xếp danh sách nlist theo thuật toán nổi bọt (Bubble Sort).
    Trả về danh sách đã sắp xếp.
    """
    for passnum in range(len(nlist)-1, 0, -1):
        for i in range(passnum):
            if nlist[i] > nlist[i+1]:
                nlist[i], nlist[i+1] = nlist[i+1], nlist[i]
    return nlist
n = int(input("Nhập số lượng phần tử của danh sách: "))
lst = list(map(int, input(f"Nhập {n} số, cách nhau bởi dấu cách: ").split()))
while len(lst) != n:
    print(f"Số lượng nhập không đúng, hãy nhập lại {n} số:")
    lst = list(map(int, input().split()))
sorted_list = bubbleSort(lst)
print("Danh sách đã sắp xếp:", sorted_list)
