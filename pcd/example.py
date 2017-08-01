#def print_msg(number):
#    def printer():
#        print("Here we are using the nonlocal keyword")
#        nonlocal number
#        number=3
#        print(number)
#    return printer
#    print(number)
#a = print_msg(9)
#a()


def a():
    print("you are inside a function")
    def b():
        print("you are inside b function")
    return b
    print("you are inside a() again...")

obj = a()
obj()

