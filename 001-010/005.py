def calculate_average(score):
	return sum(score)/len(score)
def classify_student(average):
	if average>=8.5:
		return "Xuất sắc"
	elif average>=7.0:
		return "Giỏi"
	elif average>=5.5:
		return "Khá"
	elif average>=4.0:
		return "Trung bình"
	else:
		return "yếu"
try:
	scores =[]
	num_subject = int(input("Nhập số môn học:"))
	if num_subject<=0:
		print ("Số môn học phải lớn hơn 0")
	else:		
		for i in range(num_subject):
			score = float(input(f"Nhập điểm môn học thứ {i+1}:"))
			if score>10 or score<0:
				print ("Vui lòng nhập điểm từ 0 đến 10")
				break
			scores.append(score)
		if len(scores)== num_subject:
			average_score = calculate_average(scores)
			classification = classify_student(average_score)
			print(f"Điểm trung bình :{average_score:.2f}")
			print(f"Xếp loai:{classification}")

except ValueError:
	print ("Vui lòng nhập giá trị số hợp lệ")
