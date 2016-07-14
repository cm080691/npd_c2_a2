'''Ccontains shape classes and does fun things with them

Shapes:
Triangle
Square
Circles

Data Attributes
shape_type
edge_length
name
allies
enemies

Methods:
area
perimeter
update_edge_line
add_ally
add_enemy

'''

class Triangle(object):
    shape_type = 'triangle'

    def __init__(self, edge_length, name, allies, enemies):
        self.edge_length = edge_length
        self.name = name
        self.allies = allies
        self.enemies = enemies


    def area(self):
        return self.edge_length * self.edge_length * 0.5

    def perimeter(self):
        return self.edge_length + self.edge_length + self.edge_length

    def update_edge_length(self, new_length):
        self.edge_length = new_length

    def add_ally(self, self_object):
        self.alies.append(shape_object)

    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)

if __name__ == '__main__':
    triangle_marty = Triangle(5, "marty", [], [])
    print(triangle_marty.area())
    print(triangle_marty.update_edge_length(10))
    print(triangle_marty.area())

class Square(object):
    shape_type = 'square'

    def __init__(self, edge_length, name, allies, enemies):
        self.edge_length = edge_length
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        return self.edge_length**2

    def perimeter(self):
        return self.edge_length * 4

    def update_edge_length(self, new_length):
        self.edge_length = new_length

    def add_ally(self, self_object):
        self.alies.append(shape_object)

    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)

if __name__ == '__main__':
    square_marty = Square(5, "marty", [], [])
    print(square_marty.area())
    print(square_marty.update_edge_length(10))
    print(square_marty.area())

class Circle(object):
    shape_type = 'circle'
    PI = 3.14159

    def __init__(self, edge_length, name, allies, enemies):
        self.edge_length = edge_length
        self.name = name
        self.allies = allies
        self.enemies = enemies


    def area(self):
        return self.edge_length * self.edge_length * self.PI

    def perimeter(self):
        return self.edge_length * 2 * self.PI

    def update_edge_length(self, new_length):
        self.edge_length = new_length

    def add_ally(self, self_object):
        self.alies.append(shape_object)

    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)

if __name__ == '__main__':
    circle_marty = Circle(5, "marty", [], [])
    print(circle_marty.area())
    print(circle_marty.update_edge_length(10))
    print(circle_marty.area())
