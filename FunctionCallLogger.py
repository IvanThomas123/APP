from datetime import datetime

def logger(func):
    def wrapper():
        print("Function:", func.__name__)
        print("Time:", datetime.now())
        func()
    return wrapper

@logger
def greet():
    print("Hello!")

greet()
