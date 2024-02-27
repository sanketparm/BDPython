# import os
# dir(os)

# help(os)
# import shutil
# shutil.copyfile('data.db', 'archive.db')

# shutil.move('/build/executables', 'installdir')
# import glob
# glob.glob('*.py')

# import math
# math.cos(math.pi / 4)

# math.log(1024, 2)

# import random
# random.choice(['apple', 'pear', 'banana'])

# random.sample(range(100), 10)   # sampling without replacement

# print(random.random())    # random float

# print(random.randrange(6))    # random integer chosen from range(6)

# import statistics
# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# print(statistics.mean(data))

# print(statistics.median(data))

# print(statistics.variance(data))

# dates are easily constructed and formatted
# from datetime import date
# now = date.today()
# now

# now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")


# # dates support calendar arithmetic
# birthday = date(1964, 7, 31)
# age = now - birthday
# print(age.days)

# import zlib
# s = b'witch which has which witches wrist watch'
# len(s)

# t = zlib.compress(s)
# print(len(t))

# print(zlib.decompress(t))

# print(zlib.crc32(s))

# import reprlib
# reprlib.repr(set('supercalifragilisticexpialidocious'))
# import pprint
# t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
#     'yellow'], 'blue']]]

# pprint.pprint(t, width=30)

# import locale
# locale.setlocale(locale.LC_ALL, 'English_United States.1252')

# conv = locale.localeconv()          # get a mapping of conventions
# x = 1234567.8
# locale.format_string("%d", x, grouping=True)

# print(locale.format_string("%s%.*f", (conv['currency_symbol'],
#                      conv['frac_digits'], x), grouping=True))















