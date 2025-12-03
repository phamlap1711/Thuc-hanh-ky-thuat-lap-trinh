print("Phạm Tiến Lập")
print("245752021610071")

def tim_tu_dai_nhat(ten_file):
    with open(ten_file, 'r', encoding='utf-8') as f:
        noi_dung = f.read()

    # Hàm split(): cắt chuỗi tại các khoảng trắng để tạo thành danh sách từ
    danh_sach_tu = noi_dung.split()

    if len(danh_sach_tu) == 0:
        return "File rỗng"

    do_dai_max = 0
    ket_qua = ""

    for tu in danh_sach_tu:
        do_dai = len(tu)
        if do_dai > do_dai_max:
            do_dai_max = do_dai
            ket_qua = tu

    return ket_qua

danh_sach_kq = tim_tu_dai_nhat(r"C:/Users/Tran Van Viet/Documents/7.4.py")
print(f"Từ dài nhất là: {danh_sach_kq}")
