print("Phạm Tiến Lập")
print("2455752021610071")
tu_tieng_anh = input("Nhập từ tiếng Anh viết liền nhau: ")
tutienganh_chuoi = tu_tieng_anh.split()
sap_xep = sorted(tutienganh_chuoi)
for tu in sap_xep:
    print(tu)
