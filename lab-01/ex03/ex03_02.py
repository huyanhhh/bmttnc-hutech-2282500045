def dnl(lst):
    return lst[::-1]
inputlist = input ("nhap so : ")
so =  list (map(int, inputlist(',')))
ldn = dnl(so)
print("list sau khi dao nguoc: ",ldn)

