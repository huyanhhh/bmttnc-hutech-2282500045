def dslxh(lst):
    dem = {}
    for item in lst:
        if item in dem:
            dem[item] += 1
        else:
            dem[item] = 1
    return dem
inputs = input("nhap danh sach : ")
tu = inputs.split()
slxh = dslxh(tu)
print("so lan xuat hien : ", slxh)

