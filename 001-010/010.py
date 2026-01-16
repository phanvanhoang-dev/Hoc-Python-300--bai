#import math
#a,b = map(int,input().split())
#print(math.gcd(a,b))
#print(math.lcm(a,b))
#def gcd(a, b):
#    return a if b == 0 else gcd(b, a % b)

def gcd(a,b):
  while b!=0:
    a,b = b, a%b
  return a
try:
  no1 = input("Nhập số thứ nhất:")
  no2 = input("Nhập số thứ hai:")
  result = gcd(int(no1),int(no2))
  print(f"UCLN của {no1} và {no2} là : {result} ")
except:
  print("Vui lòng nhập đúng giá trị")
