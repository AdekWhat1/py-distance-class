class Distance:
    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            value = other.km
        else:
            try: value = float(other)
            except:
                raise TypeError
        other = Distance(self.km + value)
        return other

    def __iadd__(self, other):
        if isinstance(other, Distance):
            value = other.km
        else:
            try:
                value = float(other)
            except:
                raise TypeError
        self.km += value
        return self

    def __mul__(self, other: int | float):
        if other == 0:
            raise ZeroDivisionError
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError


    def __truediv__(self, other: int | float):
        if other == 0:
            raise ZeroDivisionError
        if isinstance(other,(int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError

    def __lt__(self, other):
        if isinstance(other, Distance):
            value = other.km
        else:
            try:
                value = float(other)
            except:
                raise TypeError
        distance = bool(self.km < value)
        return distance

    def __gt__(self, other):
        if isinstance(other, Distance):
            value = other.km
        else:
            try:
                value = float(other)
            except:
                raise TypeError
        distance = bool(self.km > value)
        return distance

    def __eq__(self, other):
        if isinstance(other, Distance):
            value = other.km
        else:
            try:
                value = float(other)
            except:
                raise TypeError
        distance = bool(self.km == value)
        return distance

    def __le__(self, other):
        if isinstance(other, Distance):
            value = other.km
        else:
            try:
                value = float(other)
            except:
                raise TypeError
        distance = bool(self.km <= value)
        return distance

    def __ge__(self, other):
        if isinstance(other, Distance):
            value = other.km
        else:
            try:
                value = float(other)
            except:
                raise TypeError
        distance = bool(self.km >= value)
        return distance
