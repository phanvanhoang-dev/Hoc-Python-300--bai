def check_number(n):
	if n>0:
		return "Đây là số nguyên dương"
	elif n<0:
		return "Đây là số nguyên âm"
	else:
		return "Đây là số 0:"
try:
	number = int(input("Nhập vào một số nguyên:"))
	result = check_number(number)
	print(result)
except ValueError:
	print("Vui lòng nhập vào một số nguyên")
