square = lambda x: x * x
print(square(7))  

add = lambda a, b: a + b
print(add(5, 9))  

sign = lambda x: "Musbat" if x > 0 else "Manfiy" if x < 0 else "Nol"
print(sign(-3))  

maximum = lambda a, b: a if a > b else b
print(maximum(8, 12))  

div_by_3 = lambda x: x % 3 == 0
print(div_by_3(9)) 

mul_add = lambda x: x * 2 + 5
print(mul_add(4)) 

min_three = lambda a, b, c: a if a < b and a < c else b if b < c else c
print(min_three(7, 3, 5)) 

non_negative = lambda x: 0 if x < 0 else x
print(non_negative(-7)) 

absolute = lambda x: x if x >= 0 else -x
print(absolute(-12))  

scale_shift = lambda x: x * 5 + 7
print(scale_shift(3))  
