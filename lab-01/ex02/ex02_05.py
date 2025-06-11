sohlam = float(input("Nhap so gio lam moi tuan : "))
luonggio = float(input("Nhap thu lao tren moi gio lam tieu chuan: "))
giotieuchuan = 44
giovuotchan = max(0, sohlam - giotieuchuan)
thuclinh = giotieuchuan * luonggio + giovuotchan * luonggio * 1.5
print(f"so tien thuc linh cua nhan vien : {thuclinh}")