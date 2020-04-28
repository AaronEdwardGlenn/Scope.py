# LEGB - Local, Enclosing, Global, Built-in

x = 'global x'  # global because it is in the main body of our file

# using the global syntax for scope management


def test():
    global x    # adding this gives us the ability to modify global x in this local scope
    y = 'local y'   # y is local to our test origional_function
    print(y)
    # this can print, the local scope was looked at, then the enclosign, then global scope was looked at. x was now there.
    print(x)


test()
# print(y) this wont work.
print(x)    # this works
