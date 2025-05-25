def truy_cap_phan_tu(tuple_data):
    firstElement = tuple_data[0]
    lastElement = tuple_data[-1]
    return firstElement, lastElement
input_tuple = eval(input("Nhập một tuple các số cách nhau bằng dấu phẩy: "))
first , last = truy_cap_phan_tu(input_tuple)
print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)