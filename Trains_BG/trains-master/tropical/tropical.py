class tropical:
    def __init__(self, x):
        self._x=x

    def __add__(self, o):
        return tropical(max([self._x, o._x]))

    def __mul__(self, o):
        return tropical(self._x + o._x)

    def __str__(self):
        return str(self._x)

    def __repr__(self):
        return str(self)
