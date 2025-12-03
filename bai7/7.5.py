print("Phạm Tiến Lập")
print("245752021610071")

def file_append(ten_tep, vanban_moi):
    with open(ten_tep, 'a', encoding='utf-8') as f:
        tep_moi = f.write('\n' + vanban_moi)

    with open(ten_tep, 'r', encoding='utf-8') as f:
        noi_dung_tep = f.read()

    print("\n--- TOÀN BỘ NỘI DUNG TỆP SAU KHI NỐI ---")
    print(noi_dung_tep)

file_append(r'C:/Users/Tran Van Viet/Documents/5.4.py', 'Phạm Tiến Lập')
