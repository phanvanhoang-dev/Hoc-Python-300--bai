def count_even_odd(numbers):
    count_even = 0
    count_odd = 0
    for number in numbers:
        if number % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd

try:
    input_list = input("Nhập các số cần kiểm tra, cách nhau bởi dấu cách: ")
    numbers = [int(num) for num in input_list.split()]    
    even, odd = count_even_odd(numbers)    
    print(f"Số lượng số chẵn: {even}")
    print(f"Số lượng số lẻ: {odd}")
except ValueError:
    print("Vui lòng nhập giá trị đúng (chỉ nhập số nguyên).")
