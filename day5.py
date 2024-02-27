


# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

#------------------------------------------------------------

# words = ['cat', 'window', 'defenestrate']
# for s in words:
#     print(s, len(s))

# Create a sample collection
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# print(users)
# Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         # print("sanket")
#         del users[user]

        # print(users)

# # Strategy:  Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status

#         print(users)

# for i in range(10):
#     print(i)

# for i in list(range(5, 10)):
#     print(i)

# for i in list(range(0, 10, 3)):
#     print(i)

# for i in list(range(-10, -100, -30
# )):
#     print(i)


#-------------------------------------------------------------

# a = ['Mary', 'had', 'a', 'little', 'lamb']

# for i in range(len(a)):
#     print(i,a[i])

#-------------------------------------------------------

# x = sum(range(5))  # 0 + 1 + 2 + 3
# print(x)

#---------------------------------------------------------------

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

#-----------------------------------------------------------

# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#         # pass
# print("Found an odd number", num)

#------------------------------------------------------
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"
        
# print(http_error(int(input("Entre Port :"))))

#------------------------------------------------------
# from enum import Enum
# class Color(Enum):
#     red = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'

# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

# match color:
#     case Color.red:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues ")


# x = "python"
# y = "or"

# print(x[2:4]+y)


# x = list(range(12))

    # for i in range(x):
    #     print(i)
#  x = [10,2,3,5,4,8,7,9]

    # for i in x:
# numbers = [1, 2, 3, 4, 5]
# x = list(range(6,11))
# numbers.extend(x)
# for i in x:
#     numbers.append(i)

# print(numbers)
# for num in numbers:
#     squared = num  + 10
#     print(f"The square of {num} is {squared}")

# x = [1,2,4]

# y = [3,5,8]

# a = ['s','a','n']

# z = [x,y,a]

# print(z[0][2],z[1][1],z[2][0])

# def fibonacci(n):
#     fib_series = [0, 1]

#     while len(fib_series) < n:
#         fib_series.append(fib_series[-1] + fib_series[-2])

#     return fib_series

# # Example: Generate the first 10 Fibonacci numbers
# result = fibonacci(10)
# print(result)
#--------------------------------------------------
#searches for prime numbers:

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

#---------------------------------
# For found odd even numbers

# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number", num)
#         continue
#     print("Found an odd number", num)

#---------------------------------------

# def make_incrementor(n):
#     return lambda x: x + n

# f = make_incrementor(42)
# f(0)

# f(1)
# # print(f)

    # return fib_series

# Example: Generate the first 10 Fibonacci numbers
# result = fibonacci(10)
# print(result)


#-------------------------------------------------------

#multi-line docstring:
# def my_function():
#     """Do nothing, but document it.

#     No, really, it doesn't do anything.
#     """
#     pass

# print(my_function.__doc__)

# def f(ham: str, eggs: str = 'eggs') -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs

# f('spam')

#-------------------------------





