def count(func):
    counter = 0

    def wrapper(*args, **kwargs):
        global counter
        counter += 1
        return func(*args, **kwargs)
    return wrapper


def print_count():
    print(f'You\'ve called functions {counter} times')