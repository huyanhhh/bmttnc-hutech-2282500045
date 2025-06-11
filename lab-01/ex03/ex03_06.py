def xpt(dictionary, key):
    if key in dictionary:
       del dictionary[key]
       return True
    else:
        return False
my = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
keydetele = 'b'
result = xpt (my, keydetele)
if result:
    print("phan tu da dc xoa : ", my)
else:
    print("kh tim thay ")
    
    



    