import random


class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides")
        if not isinstance(sides, int):
            # make sure sides is a int
            raise ValueError("Sides must be a whole number")
        self.value = value or random.randint(1, sides)

    def __int__(self):
        return self.value

    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        return int(self) != other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) > other or int(self) == other

    def __le__(self, other):
        return int(self) < other or int(self) == other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)


class D6(Die):
    def __init__(self, sides=2, value=0):  # current class
        super().__init__(sides=6, value=value)


# d = Die(sides=6)
# print(d.value)
#
# d2 = D6()
# print(d2.value)
#
# d6 = D6()
# print(d6 > 1)
#
# d7 = D6()
# print(d7 + d2)
