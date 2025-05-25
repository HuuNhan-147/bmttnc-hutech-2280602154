
from QuanLySinhVien import QuanLySinhVien
qlsv=QuanLySinhVien()
print("\nCHUONG TRỊNH QUAN LÝ SINH VIEN")
while (1==1):
    print("********************MENU***************************")
    print("** 1. Them sinh vien.                            **")
    print("** 2. Cap nhat thong tin sinh vien boi ID.       **") 
    print("** 3. Xoa sinh vien boi ID.                      **")
    print("** 4. Tim kiem sinh vien theo ten.               **")
    print("** 5. Sap xep sinh vien theo diem trung bình.    **")
    print("** 6. Sap xep sinh vien theo ten chuyen nganh.   **")
    print("** 7. Hiền thì danh sach sinh vien.              **")
    print("** 0. Thoat                                      **")
    print("***************************************************")
    key = int(input("Nhap tuy chọn: "))
    if (key==1):
        print("\n1. Them sinh viên.") 
        qlsv.nhapSinhVien()
        print("\nThem sinh viên thanh công!")
        
    elif (key==2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cap nhất thông tin sinh vien. ")
            print("\nNhap ID: ")
            ID=int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nSanh sách sinh viên trong")
    elif (key==3):
        if (qlsv.soLuongSinhVien() >0):
            print("\n3. Xoa sinh vien.") 
            print("\nNhap ID: ")
            ID= int(input())
            if(qlsv.deleteById(ID)):
                print("\nSinh vien co id =", ID, " da bi xoa.")
            else:
                print("\nSinh vien co id = ", ID," khong ton tai.")
        else:
            print("\nSanh sách sinh vien trong!")
    elif (key== 4):
        if (qlsv.soLuongSinhVien() > 0):      
            print("\n4. Tim kiem sinh vien theo ten.") 
            print("\nNhap ten de tim kiem: ") 
            name= input()
            searchResult = qlsv.findByName(name) 
            qlsv.showSinhVien (searchResult)
        else: 
            print("\nSanh sạch sinh vien trong!")
    elif (key== 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5, Sap xep sinh vien theo diem trung bình (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien (qlsv.getListSinhVien())
        else:
            print("\nSanh sạch sinh vien trong!")
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6, Sap xep sinh vien theo ten. ") 
            qlsv.sortByName()
            qlsv.showSinhVien (qlsv.getListSinhVien())
        else:
            print("\nSanh sạch sinh vien trong ")
    elif (key==7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sạch sinh vien.") 
            qlsv.showSinhVien (qlsv.getListSinhVien())
        else:
            print("\nSanh sach sinh viên trong :")
    elif (key== 0):
        print("\nBan da chọn thoát chuơng trình!")
        break
    else:
        print("\nkhong co chuc nang nay!")
        print("\nHay chon chuc nang trong hop menu.")
   