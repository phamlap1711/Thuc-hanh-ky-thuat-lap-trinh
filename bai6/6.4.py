print("Pham Tien Lap")
print("248752021610071")
class RomanNumber:
    # Bảng giá trị của ký tự La Mã
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    # Hàm khởi tạo
    def __init__(self, roman):
        self.roman = roman.upper()   # đưa chuỗi về chữ in hoa
    # Phương thức đổi số La Mã sang số nguyên
    def toInteger(self):
        total = 0
        prev_value = 0
        # Duyệt từng ký tự từ phải sang trái
        for char in reversed(self.roman):
            value = self.roman_values[char]
            # Nếu giá trị nhỏ hơn giá trị phía trước → phải trừ (IV = 4)
            if value < prev_value:
                total -= value
            else:
                total += value

            prev_value = value

        return total
# Chương trình chính
s = input("Nhập số La Mã: ")
obj = RomanNumber(s)
print("Giá trị số nguyên:", obj.toInteger())
