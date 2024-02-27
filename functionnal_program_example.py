# Example of using map() and lambda functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Example of using filter() and lambda functions
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Example of list comprehension
cubes = [x ** 3 for x in numbers]
print(cubes)  # Output: [1, 8, 27, 64, 125]

# Example of recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))  # Output: 120
