def print_max(x,y):
    '''Prints the maximum of two numbers.

    The two values must be integers'''
    # convert to integers, if possible
    if x>y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'
print_max(3, 6)
print print_max.__doc__


help(print_max)
