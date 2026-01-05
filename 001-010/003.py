def find_maxnumber_of_three(a, b, c):
	if a>=b and a>=c:
		return a
	elif b>=a and b>=c:
		return b
	else:
		return c
try:
	num1 = int(input("Nhập số thứ nhất:"))
	num2 = int(input("Nhập số thứ hai:"))
	num3 = int(input("Nhập số thứ ba:"))
	result = find_maxnumber_of_three(num1, num2, num3)	
	print(result)
except ValueError:
	print("Vui lòng nhập lại giá trị là số")
