from decorators.square import Square


@Square
def add_one(x):
    return add_one_without_decorator(x)


def add_one_without_decorator(x):
    return x + 1


@Square
def add_two_numbers(x, y):
    return x + y


if __name__ == '__main__':
    print(add_one(10))
    print(add_two_numbers(20, 30))
    print(add_two_numbers(y=15, x=10))
