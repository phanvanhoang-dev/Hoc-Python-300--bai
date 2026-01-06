def calculate_total_money(km):
	if km <=1:
		fare = 10000
	elif km<=10:
		fare = 10000+ (km-1)*8500
	else:
		fare = (10000+9*8500)+(km-10)*7500
	return fare
try:
	distance = float(input("Nhập số km đã đi:"))
	if distance <=0:
		print("Vui lòng không nhập số âm để trêu máy")
	else:
		result = calculate_total_money(distance)
		print(f"Tổng tiền phải trả là {result}")

except ValueError:
	print("Vui lòng nhập kí tự có giá trị là số")
