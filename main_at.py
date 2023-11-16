def operate(func):
    def poo_bum(*args, **kwargs):
        print('You have called the decorator')
        result = func(*args, **kwargs)
        print('I have just called the function for you')
        return result
    return poo_bum


@operate
def add_one(x):
    return x + 1


@operate
def add_two_numbers(x, y):
    return x + y


if __name__ == '__main__':
    # print(add_one(10))
    print(add_two_numbers(20, 30))
    # print(add_two_numbers(y=15, x=10))
