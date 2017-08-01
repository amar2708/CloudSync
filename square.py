def square(n):
    return n*n

x = [1,5,6,7]

print (list(map(square, x)))

print ([x*x for x in range(10)])
