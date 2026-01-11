def Kiem_tra_nam(year):
  if year % 400 ==0 or year %4 ==0 and year % 100 !=0:
    return "Đây là năm nhuận"
  else:
    return "Đây không phải là năm nhuận"
try:
  year = int(input("Nhập năm:"))
  if year <0:
    print("Vui lòng nhập năm sau công nguyên")
  result=Kiem_tra_nam(year)
  print(result)
except ValueError:
  print("Vui lòng nhập đúng giá trị cần kiểm tra")
