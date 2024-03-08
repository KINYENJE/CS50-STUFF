# This file is created to understand the concept of decorators in python and how to use them.
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

# this is a decorator that will be used to decorate hello function
@announce
def hello():
    print("Hello, world!")

hello()