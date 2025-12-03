print("Pham Tien Lap")
print("248752021610071")
class StringManipulator:
    """Class đơn giản để lấy chuỗi từ người dùng và in hoa."""

    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("Nhập chuỗi của bạn: ")

    def print_string(self):
        print("Chuỗi in hoa:", self.s.upper())
# Tạo đối tượng của lớp
manipulator = StringManipulator()
manipulator.get_string()
manipulator.print_string()
