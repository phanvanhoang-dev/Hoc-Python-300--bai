def calculate_average(scores):
	return sum(scores)/len(scores)
def classify_student(average):
	if average >=8:
		return "Xuất Sắc"
	elif average >=7:
		return "Giỏi"
	elif average >=5.5:
		return "Khá"
	elif average >=4:
		return "Trung bình"
	else:
		return "Yếu"
try:
	scores=[]
	num_subject = int(input("Nhập số môn học:"))
	if num_subject <=0:
		print ("Vui lòng nhập số môn lớn hơn 0")
	else:	
		for i in range(num_subject):
			score = float(input(f"Nhập điểm môn thứ {i+1} :"))
			if score <0 or score >10:
				print("Vui lòng nhập điểm từ 0 đến 10")
				break
			scores.append(score)
		if len(scores) == num_subject:
			average_score = calculate_average(scores)
			classification = classify_student(average_score)
			print(f"Điểm trung bình : {average_score}")
			print(f"Xếp loại: {classification}")
except ValueError:
	print("Vui lòng nhập giá trị số:")
