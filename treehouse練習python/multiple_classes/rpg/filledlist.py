import copy

class FilledList(list):
    def __init__(self, count, value, *args, **kwarg):
        super().__init__()  # use empty list
        for _ in range(count):
            self.append(copy.copy(value))
