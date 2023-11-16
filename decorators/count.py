counter = 0


def count(func):
    def wrapper(*args, **kwargs):
        global counter
        counter += 1
        return func(*args, **kwargs)
    return wrapper


def print_count():
    print(f'You\'ve called functions {counter} times')