class Calic:
    def __init__(self, a):
        self.a = a

    def __add__(self, a, other):
        return self.a + other

    def __sub__(self, a, other):
        other - self.a

    def __mul__(self, a, other):
        other * self.a

    def __truediv__(self, a, other):
        other / self.a


c = Calic(12)
c.__add__(12, 12)
c.__sub__(12, 12)
c.__mul__(12, 12)
c.__truediv__(12, 12)
