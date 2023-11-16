from decorators.timer import Timer


@Timer
def add_lots_of_numbers():
    total = 0
    for x in range(0, 100000000):
        total += x
    print(total)


if __name__ == '__main__':
    add_lots_of_numbers()
