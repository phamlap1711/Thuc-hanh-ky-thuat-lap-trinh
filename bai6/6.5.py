print("Pham Tien Lap")
print("248752021610071")

class StringReverse:
    def __init__(self, input_str):
        self.input_str = input_str

    def reverse_words(self):
        # Tách chuỗi thành danh sách các từ
        words = self.input_str.split()

        # Đảo ngược danh sách từ
        reversed_words = words[::-1]

        # Ghép chuỗi lại
        return " ".join(reversed_words)


# Chương trình chính
chuoI = input("Nhập chuỗi: ")

obj = StringReverse(chuoI)
print("Chuỗi sau khi đảo lại:", obj.reverse_words())
