print("Pham Tien Lap")
print("248752021610071")

class HinhChuNhat(object):
    def __init__(self, chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong

    def area(self):
        return self.chieudai * self.chieurong

hinhchunhat = HinhChuNhat(7, 3)
print(hinhchunhat.area())
