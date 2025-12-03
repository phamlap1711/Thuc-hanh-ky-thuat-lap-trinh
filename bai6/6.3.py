print("Pham Tien lap")
print("248752021610071")
class GioiTinh(object):
    def getGender(self):
        return "unknown"
class Nam(GioiTinh):
    def getGender(self):
        return "nam"
class Nu(GioiTinh):
    def getGender(self):
        return "nu"
aNam = Nam()
aNu = Nu()
print(aNam.getGender())
print(aNu.getGender())
