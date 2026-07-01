from functools import wraps

def my_decor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Before the call')
        func(*args, **kwargs)
        print('After the call')
    return wrapper


def say_hello(name, surname='Guest'):
    print('Hi ' + name + ' ' + surname)


say_hello = my_decor(say_hello)

say_hello('igor', surname='oshust')