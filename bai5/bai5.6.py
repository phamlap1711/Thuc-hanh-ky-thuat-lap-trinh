def sap_xep(ds):
    """Hàm sắp xếp danh sách tăng dần"""
    return sorted(ds)

def tim_max(ds):
    """Hàm tìm phần tử lớn nhất"""
    return max(ds)

def tim_min(ds):
    """Hàm tìm phần tử nhỏ nhất"""
    return min(ds)

# --- Chương trình chính ---
n = int(input("Nhập số lượng phần tử của danh sách: "))

ds = []
for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i+1}: "))
    ds.append(x)

print("\nDanh sách ban đầu:", ds)

# Gọi các hàm xử lý
ds_sap_xep = sap_xep(ds)
lon_nhat = tim_max(ds)
nho_nhat = tim_min(ds)

# Tìm vị trí (index) của phần tử lớn nhất và nhỏ nhất
vi_tri_max = ds.index(lon_nhat)
vi_tri_min = ds.index(nho_nhat)

# In kết quả
print("Danh sách sau khi sắp xếp:", ds_sap_xep)
print("Phần tử lớn nhất:", lon_nhat, "ở vị trí:")
