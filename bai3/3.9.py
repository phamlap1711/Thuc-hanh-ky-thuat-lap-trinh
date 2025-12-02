print("Phạm Tiến Lập")
print("245752021610071")
def benefit(t, n, k):
    r = t / 100        # lãi suất theo %
    so_tien_nhan_duoc = n * (1 + r) ** k
    return so_tien_nhan_duoc
print(benefit(2, 400000, 5))
