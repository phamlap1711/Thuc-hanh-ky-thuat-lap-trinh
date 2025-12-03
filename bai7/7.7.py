print("Phạm Tiến Lập")
print("245752021610071")

def demsodong(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        return len(lines)

print("Tổng số dòng là:", demsodong(r'C:/Users/Tran Van Viet/Documents/5.4.py'))
