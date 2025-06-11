def tcpt(tuple_data):
    f_element = tuple_data[0]
    l_element = tuple_data[1]
    return f_element, l_element
input_tuple = eval(input("nhap tuple : "))
f, l = tcpt(input_tuple)
print("phan tu dau tien : ", f)
print("phan tu dau tien : ", l)