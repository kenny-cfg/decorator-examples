from decorators.count import count, print_count


@count
def add_one(x):
    return x + 1


@count
def add_two_numbers(x, y):
    return x + y


if __name__ == '__main__':
    print(add_one(10))
    print(add_two_numbers(20, 30))
    print(add_two_numbers(y=15, x=10))
    print_count()
