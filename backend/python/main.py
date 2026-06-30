class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return Vector(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1_x, v1_y = 3.0, 4.0
v2_x, v2_y = 1.0, 2.0

v1 = Vector(v1_x, v1_y)
v2 = Vector(v2_x, v2_y)

print(v1)         # Строковое представление
print(v2)         # Строковое представление
print(v1 + v2)    # Сложение векторов
print(v1 == v2)   # Сравнение векторов