# LEGB - Local, Enclosing, Global, Built-in
import builtins
x = 'global x'  # global because it is in the main body of our file

print(dir(builtins))    # gives us a list of all builtins

# NOTE it is possible to overwrite our builtins, so be careful to not name anything the same name as a default.


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


test('local z')
# print(y) this wont work.
print(x)    # this works

# enclosing scope has to do with nested functions.


def outter():
    x = 'outter x'

    def inner():
        nonlocal x  # this allows us to access the variables in the outside scope of this nested function. the result of line 41 would then be 'inner x' twice. because it would override the line 33's declaration of x as 'outter x'
        # x = 'inner x'
        print(x)

    inner()
    print(x)


outter()

# so in this example. line 36 will print inner x and then line 40 will print outer x. when we comment out line 36, we get two 'outter x' print statements occuring.

# enclusing scope is just saying that, in nested funcitons, the scope of the outter function is checked after teh scope of the inner function.
