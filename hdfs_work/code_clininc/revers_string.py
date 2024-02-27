def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

# Example usage:
input_str = "Hello, world!"
reversed_str = reverse_string(input_str)
print(reversed_str)  # Output: "!dlrow ,olleH"
