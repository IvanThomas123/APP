def call_counter(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print("Function called", count, "times")
        func()

    return wrapper

@call_counter
def hello():
    print("Hello")

hello()
hello()
hello()
