def tttl(lst):
    return tuple(lst)
inputl = input("nhap danh sach: ")
so = list(map(int, inputl(',')))
my = tttl(so)
print("list : ", so)
print("tuple tu list : ", my)
