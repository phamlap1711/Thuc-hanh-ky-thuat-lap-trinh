print("Phạm Tiến Lập")
print("245752021610071")
chuoi_nhap = input("Nhập các từ: ")
danh_sach_tu = chuoi_nhap.split()
if not danh_sach_tu:
    print("Không có từ nào được nhập.")
else:
    # Tìm độ dài lớn nhất
    do_dai_lon_nhat = max(len(tu) for tu in danh_sach_tu)

    # Tìm các từ có độ dài lớn nhất
    tu_dai_nhat = []
    for tu in danh_sach_tu:
        if len(tu) == do_dai_lon_nhat:
            tu_dai_nhat.append(tu)
    # Loại bỏ các từ trùng nhau bằng set
    tu_dai_nhat_khong_trung = list(set(tu_dai_nhat))
    print("Độ dài lớn nhất:", do_dai_lon_nhat)
    print("Từ dài nhất (hoặc các từ có cùng độ dài):", tu_dai_nhat_khong_trung)
