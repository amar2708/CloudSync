# tuple once declared can not be modified....if we try to do so...it will throw
# an error.

tup = (1, 2, 3, 4)
print(id(tup))
tup[0] = 5      #it will throw an error

#however if we try to do this
tup = (6, 7, 8, 9)
print(id(tup))
#the original tuple is not changed...but a new tuple is created and previous
#tuple is garbage collected






#however a list element can be modified....
lst = [10, 20, 30, 40]
print(id(lst))

#in list element at particular position can be modified..
lst[1] = 50     #the list element wil get modified.
print(id(lst))

