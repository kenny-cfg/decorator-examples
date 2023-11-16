def operate(func):
    def poo_bum(x):
        print('You have called the decorator')
        result = func(x)
        print('I have just called the function for you')
        return result
    return poo_bum


@operate
def add_one(x):
    return x + 1


@operate
def subtract_one(x):
    return x - 1


if __name__ == '__main__':
    print(add_one(10))
    print(subtract_one(20))
