from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def generateID(self):
        maxId = 1
        if self.soLuongSinhVien() > 0:
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if maxId < sv._id:
                    maxId = sv._id
            maxId += 1
        return maxId

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành của sinh viên: ")
        diemTB = float(input("Nhập điểm trung bình của sinh viên: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = input("Nhập chuyên ngành của sinh viên: ")
            diemTB = float(input("Nhập điểm trung bình của sinh viên: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print(f"Sinh viên có ID = {ID} không tồn tại.")

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=True)

    def findByID(self, ID):
        searchResult = None
        for sv in self.listSinhVien:
            if sv._id == ID:
                searchResult = sv
                break
        return searchResult

    def findByName(self, keyword):
        listSV = []
        for sv in self.listSinhVien:
            if keyword.upper() in sv._name.upper():
                listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocLuc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Khá"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<15} {:<8} {:<10}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<15} {:<8.2f} {:<10}".format(
                sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc
            ))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien
