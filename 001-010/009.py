def is_prime(n):
    if n <=1:
        return False
    for i in range(2, int(n**0.5) +1):
        if n % i == 0:
            return False
    else:
        return True
def print_prime_up_to_100():
    for number in range(1, 101):
        if is_prime(number):
            print(number, end=', ')
print_prime_up_to_100()
