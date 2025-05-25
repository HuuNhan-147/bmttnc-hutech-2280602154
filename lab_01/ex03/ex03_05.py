def dem_so_lan_xuat_hien(lst):   
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
input_list = input("Nhập danh sách các số cách nhau bằng dấu phẩy: ")
word_list = input_list.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("So lan xuat hien cua cac phan tu trong list:", so_lan_xuat_hien)