class Square:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print('Inside the Square decorator')
        result = self.function(*args, **kwargs)
        print(f'Result of the function call is {result}')
        return result * result
