# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    # the exception type
#     print(inst.args)     # arguments stored in .args
#     print(inst)          # __str__ allows args to be printed directly,
#                          # but may be overridden in exception subclasses
#     x, y = inst.args     # unpack args
#     print('x =', x)
#     print('y =', y)

# def this_fails():
#     x = 1/0

# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)




# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')

# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")

# divide(2, 1)


# divide(2, 0)


# divide("2", "1")

# def func():
#     raise ConnectionError

# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc