squares = [1, 4, 9, 16, 25]
print("v1",squares[0])
print("v2",squares[-1])

print("v3",squares[-3:])  # slicing returns a new list

a = squares + [36, 49, 64, 81, 100]

print("v4",a)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print("v5",letters)


# replace some values
# letters[2:5] = ['C', 'D', 'E']
# print("v6",letters)

# letters[2:5] = []
# print("v7",letters)

# letters[:] = []
# print("v8",letters)

# print("v9",len(letters))


# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1

while a < 10:
    print(a)
    a, b = b, a+b