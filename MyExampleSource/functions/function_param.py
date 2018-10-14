def print_max(a, b):
    if a>b:
        print a, 'is maximum'
    elif a==b:
        print a, 'is equal to', b
    else:
        print b, 'is maximum'


print_max(6, 4)

x = 5
y = 7

print_max(x, y)

y = 5

print_max(x, y)