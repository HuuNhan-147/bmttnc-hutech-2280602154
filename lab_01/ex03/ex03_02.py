def dao_nguoc_chuoi_list(lst):
    return lst[::-1]


input_list  =input("nhập vào danh sách các số ,các nhau bằng dấu phẩy : ")
numbers = list(map(int,input_list.split(',')))

list_dao_nguoc = dao_nguoc_chuoi_list(numbers)
print("List sau khi đảo ngược : ",list_dao_nguoc)