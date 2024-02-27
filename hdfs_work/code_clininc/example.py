# # Create a list of numbers from 1 to 10
# numbers = list(range(1, 11))

# # Iterate through the list and print even numbers
# for num in numbers:
#     if num % 2 == 0:
#         print(num)

def split_string_into_words(input_string):
    # Split the string into words using whitespace as the separator
    words = input_string.split()
    return words

# Example usage:
input_string = "the quick brown fox jumps over the lazy dog"
word_list = split_string_into_words(input_string)
print(word_list)

