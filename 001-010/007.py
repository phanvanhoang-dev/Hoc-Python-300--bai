def is_leap_year(year):
  return (year % 4==0 and year % 100 !=0) or ( year % 400==0)
try:
  year = int(input("Nhập năm cần kiểm tra:"))
  if is_leap_year(year):
    print(f"{year} Đây là năm nhuận")
  else:
    print(f"{year} Đây không phải năm nhuận")
except ValueError:
  print("Vui lòng nhập giá trị hợp lệ")
