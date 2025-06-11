def ttsc(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong
inputlist = input("nhap danh sach cac so, cach nhau bang sau phay: ")
so = list(map(int, inputlist.split(',')))
tongchan = ttsc(so)
print("tong so chan : ", tongchan)

