# -- Print Functions --
# - 3.1 Say Goodbye -
def say_goodbye(name):
     print("Goodbye, ", name)
    
     print(say_goodbye("Allie"))

# - 3.2 Area of a Circle -
def area_of_circle(radius):
     area = 3.14 * radius * radius
     return area
print(area_of_circle(5))

# -- Return Functions --
# - 4.1 Subtract, Multiply, Divide -
def subtract(x, y):
     return x - y
print(subtract(10, 5))
def multiply(x, y):
     return x * y
print(multiply(10, 5))
def divide(x, y):
     return x / y
print(divide(10, 5))

# -- Conditionals --
# - 5.1 What Should I Wear? -
readings = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
min_temp = min(readings)
max_temp = max(readings)
def temp_check(temp):
    max_temp = max(readings)
    min_temp = min(readings)
    return (min_temp, max_temp)
print(temp_check(readings))

# - 5.2 Check if it's the Weekend -
def weekend_check(day):
        if day == 6 or day == 7:
            return True
        else:
            return False
print(weekend_check(6))

     
# - 5.3 Fuel Efficiency Calculator -
def fuel_efficiency(miles, gallons):
        return miles / gallons
print(fuel_efficiency(300, 10))

# - 5.4 Secret Code -
def secret_code(n):
    last_digit = n % 10        
    rest = n // 10             
    digits = len(str(rest))    
    return last_digit * (10 ** digits) + rest
print(secret_code(1234))

# -- Loops --
# - 6.1 Oski Stole Your Power -
def power_stolen(x, y):
     result = 1
     for iteration in range(y):
          result *= x
     return result
print(power_stolen(2, 4))

# - 6.2 Min & Max with Loops -
# 6.2.1 For Loops
num = range(0,11,1)
def minimum(num):
     for i in num:
        if i < 5:
             return "Minimum is:", i
print(minimum(num))

def maximum(num):
     for i in num:
          if i > 5:
               return "Maximum is: ", i
print(maximum(num))

# 6.2.2 While Loops
def minimum_2(num):
     i = 0
     while i < len(num):
          if num[i] < 5:
               return "Minimum is: ", num[i]
          i += 1
print(minimum_2(num))
def maximum_2(num):
     i = 0
     while i < len(num):
          if num[i] > 5:
               return "Maximum is: ", num[i]
          i += 1
print(maximum_2(num))

# - 6.3 Calculate the Sum -
def calculate_sum(n):
    n = abs(n)          
    total = 0
    
    while n > 0:
        total += n % 10   
        n //= 10          
        
    return total
print(calculate_sum(234))

# I choose What Should I Wear as my favorite!