class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

    def __radd__(self, other):
        return self + other
    # python 會自動幫你 swap 所以 self +other 即可
    # reflect number + 1

    def __iadd__(self, other):
        self.value = self + other
        return self.value
    #  inplace number += 1
    # age = Numstring(25)
    # age +1 =?  => 26