print("Pham Tien Lap")
print("248752021610071")
import timkiem
# Hàm nhập dữ liệu
def nhap_du_lieu():
    while True:
        try:
            input_str = input("Nhập các số nguyên (cách nhau bằng khoảng trắng): ")
            lst = [int(x) for x in input_str.split()]
            return lst
        except ValueError:
            print("Lỗi! Vui lòng chỉ nhập số nguyên.")
# ================= MAIN =================
if __name__ == "__main__":
    # Nhập danh sách gốc
    danh_sach_goc = nhap_du_lieu()
    # Nhập giá trị cần tìm
    gia_tri = int(input("Nhập phần tử cần tìm: "))
    # Sao chép danh sách để sắp xếp
    danh_sach_da_sap_xep = danh_sach_goc.copy()
    danh_sach_da_sap_xep = timkiem.timsort(danh_sach_da_sap_xep)
    # Tìm kiếm nhị phân
    ket_qua = timkiem.tim_nhi_phan(danh_sach_da_sap_xep, gia_tri)
    # Xuất kết quả
    print("\nDanh sách ban đầu:", danh_sach_goc)
    print("Danh sách đã sắp xếp:", danh_sach_da_sap_xep)
    if ket_qua != -1:
        print(f"Giá trị {gia_tri} được tìm thấy tại vị trí index {ket_qua}.")
    else:
        print("Không tìm thấy!")
