# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']


# print(a)
# b = fruits.count('tangerine')
# print(b)

# print(fruits.index('banana'))

# print(fruits.index('banana', 4))  # Find next banana starting at position 4

# print(fruits.reverse())
# fruits

# fruits.append('grape')
# print(fruits)

# fruits.sort()
# print(fruits)

# fruits.pop()
# print(fruits)

# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# stack.pop()
# print(stack)

# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# queue.popleft()                 # The first to arrive now leaves

# queue.popleft()                 # The second to arrive now leaves

# print(queue)                     # Remaining queue in order of arrival

# squares = []
# for x in range(10):
#     squares.append(x**2)
    
# print(squares)

# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))

# print(combs)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# print(matrix)
# a = [[row[i] for row in matrix] for i in range(4)]

# print(a)

# transposed = []
# for i in range(4):
#     transposed.append([row[i] for row in matrix])

# print(transposed)


#del stattement

# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]


# del a[2:4]


# # del a[:]
# print(a)

# t = 12345, 54321, 'hello!'
# print(t[0])
# Tuples may be nested:
# u = t, (1, 2, 3, 4, 5)
# print(u)
# Tuples are immutable:

# print(t[0])
# but they can contain mutable objects:
# v = ([1, 2, 3], [3, 2, 1])
# print(v)

# empty = ()
# singleton = 'hello',    # <-- note trailing comma
# print(singleton)
# len(empty)

# len(singleton)

# print(singleton)

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# # print(basket)                      # show that duplicates have been removed

# a = 'crabgrass' in basket
# print(a)


#dictonaryss 

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel['jack']

del tel['sape']
tel['irv'] = 4127
print(tel)



