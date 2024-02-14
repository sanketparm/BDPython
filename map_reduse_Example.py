from functools import reduce
from multiprocessing import Pool
from collections import defaultdict
import re

def map_func(line):
    word_count = defaultdict(int)
    words = re.findall(r'\w+', line.lower())
    for word in words:
        word_count[word] += 1
    return word_count

def reduce_func(count1, count2):
    for word, freq in count2.items():
        count1[word] += freq
    return count1

def mapreduce(data, num_processes):
    pool = Pool(num_processes)
    mapped_data = pool.map(map_func, data)
    reduced_data = reduce(reduce_func, mapped_data)
    return reduced_data

if __name__ == "__main__":
    # Read input data from a text file
    with open(r'C:\Users\sanke\OneDrive\Documents\BDPython\sample1.txt', 'r') as file:

        input_data = file.readlines()

    # Define the number of processes for parallel processing
    num_processes = 4

    # Perform MapReduce
    word_counts = mapreduce(input_data, num_processes)

    # Output the word counts
    for word, count in word_counts.items():
        print(f"{word}: {count}")
