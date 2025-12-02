print("Phạm Tiến Lập")
print("245752021610071")
def get_sum(*num):
    tmp = 0
    # duyệt các tham số
    for i in num:
        tmp += i
    return tmp
result = get_sum(1, 2, 3, 4, 5)
print(result)
