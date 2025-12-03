print("Pham Tien Lap")
print("248752021610071")
import numpy as np
# Hàm nhập danh sách số nguyên
def nhap_danh_sach():
    while True:
        try:
            input_str = input("Nhập danh sách các số (cách nhau bằng dấu cách): ")

            # Chuyển chuỗi nhập vào thành list các số nguyên
            danh_sach = [int(x) for x in input_str.split()]
            return danh_sach

        except ValueError:
            print("Lỗi! Vui lòng chỉ nhập số nguyên và cách nhau bằng dấu cách!\n")
# ================= MAIN =================
if __name__ == "__main__":
    # Nhập danh sách
    danh_sach = nhap_danh_sach()
    # Nhập phần tử cần tìm
    item_can_tim = int(input("Nhập phần tử (item) cần tìm trong danh sách: "))
    # Dùng sequential_search của numpy
    ket_qua = np.where(np.equal(danh_sach, item_can_tim))[0]
    # Xử lý kết quả tìm kiếm
    if len(ket_qua) > 0:
        vi_tri = ket_qua[0]
        print(f"Tìm thấy {item_can_tim} tại vị trí index [{vi_tri}].")
        print(f"Phần tử này lấy từ danh sách: {danh_sach[vi_tri]}")
    else:
        print(f"Không tìm thấy {item_can_tim} trong danh sách!")
