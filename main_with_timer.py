from decorators.timer import Timer


@Timer
def add_lots_of_numbers():
    total = 0
    for x in range(0, 100000):
        total += x
    return total


if __name__ == '__main__':
    print(add_lots_of_numbers())
