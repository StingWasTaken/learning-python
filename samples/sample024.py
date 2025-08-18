# Read-Only Attributes with the property attribute
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


point = Point(1, 2)
print(f"Point coordinates: ({point.x}, {point.y})")
point.x = 10  # This will raise an AttributeError