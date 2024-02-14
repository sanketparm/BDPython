# Example 1: Function that takes another function as an argument
def apply_operation(func, x, y):
    return func(x, y)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

result1 = apply_operation(add, 3, 5)
print("Result of addition:", result1) 

result2 = apply_operation(subtract, 7, 2)
print("Result of subtraction:", result2) 

# Example 2: Function that returns another function
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

multiply_by_2 = create_multiplier(2)
result3 = multiply_by_2(5)
print("Result of multiplication by 2:", result3)  

multiply_by_3 = create_multiplier(3)
result4 = multiply_by_3(5)
print("Result of multiplication by 3:", result4) 
