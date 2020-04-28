# LEGB - Local, Enclosing, Global, Built-in

x = 'global x'  # global because it is in the main body of our file

# NOTE an iterable is anything that can be returned one at a time. so a list, tuple, or set
# using the global syntax for scope management
m = min([1, 2, 3])
print(m)


def test(z):    # z is also local to this function
    global x    # adding this gives us the ability to modify global x in this local scope
    y = 'local y'   # y is local to our test origional_function
    print(y)
    # this can print, the local scope was looked at, then the enclosign, then global scope was looked at. x was now there.
    print(x)
    print(z)


test('local z')  # this enclosing scope we reference
# print(y) this wont work.
print(x)    # this works
