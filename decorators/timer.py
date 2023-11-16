import time


class Timer:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        start_time = time.perf_counter()
        result = self.function(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f'The function took {duration} seconds')
        return result