print("Phạm Tiến Lập")
print("245752021610071")
from math import sqrt
a = int(input("Nhập giá trị của a: "))
b = int(input("Nhập giá trị của b: "))
c = int(input("Nhập giá trị của c: "))
if a == 0:
    # Phương trình trở thành bx + c = 0
    if b == 0:
        print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print("Phương trình có nghiệm x =", x)
else:
    delta = b*b - 4*a*c

    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x =", x)
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        print("Phương trình có nghiệm x1 =", x1)
        print("Phương trình có nghiệm x2 =", x2)
