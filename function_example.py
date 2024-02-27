# def fib(n):    # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# # Now call the function we just defined:
# fib(100)

#-------------------------------------------
# def foo(name, **kwds):
#     return 'name' in kwds
# foo(1, **{'name': 2})

# def standard_arg(arg):
#     print(arg)

# def pos_only_arg(arg, /):
#     print(arg)

# def kwd_only_arg(*, arg):
#     print(arg)

# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)

# standard_arg(2)

# standard_arg(arg=2)

# pos_only_arg(1)
# pos_only_arg(arg=1)

#---------------------------------------------

# def write_multiple_items(file, separator, *args):
#     file.write(separator.join(args))


def concat(*args, sep="/"):
    return sep.join(args)
    

concat("earth", "mars", "venus")

concat("earth", "mars", "venus", sep=".")

