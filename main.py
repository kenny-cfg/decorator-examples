def add_one(x):
    return x + 1


def subtract_one(x):
    return x - 1


def operate(func, x):
    print('You have called the decorator')
    return func(x + 1)


if __name__ == '__main__':
    print(operate(add_one, 10))
    print(operate(subtract_one, 20))