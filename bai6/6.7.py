print("Pham Tien Lap")
print("248752021610071")
import math
class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Bán kính không thể là số âm hoặc bằng 0.")
        self.radius = radius

    def calculate_area(self):
        """Tính diện tích hình tròn."""
        area = math.pi * (self.radius ** 2)
        return area

    def calculate_perimeter(self):
        """Tính chu vi hình tròn."""
        perimeter = 2 * math.pi * self.radius
        return perimeter
# Chương trình chính
my_circle = Circle(5)
area = my_circle.calculate_area()
print(f"Diện tích hình tròn (radius=5) là: {area:.2f}")
perimeter = my_circle.calculate_perimeter()
print(f"Chu vi hình tròn (radius=5) là: {perimeter:.2f}")
