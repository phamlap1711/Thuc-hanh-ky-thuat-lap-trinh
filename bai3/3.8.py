print("Phạm Tiến Lập")
print("245752021610071")
import math
def Tinh(R):
    if R <= 0:
        print("Xin hãy nhập R là số dương!")
        return
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R * R
    print("Chu vi hình tròn =", chu_vi)
    print("Diện tích hình tròn =", dien_tich)
R = int(input("Nhập bán kính hình tròn: "))
Tinh(R)

# Muốn tính khi R bằng mấy thì thay vào vị trí R
