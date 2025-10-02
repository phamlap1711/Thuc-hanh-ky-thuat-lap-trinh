import math
a = float(input("Nhap he so a (khác 0): "))
b = float(input("Nhap he so b: "))
c = float(input("Nhap he so c: "))
if a == 0:
    print("Day khong phai la phuong trinh bac 2.")
else:    
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phuong trinh co hai nghiem phan biet:\nx1 = {x1}\nx2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phuong trinh co nghiem kep:\nx = {x}")
    else:
        print("Phuong trinh vo nghiem.")
