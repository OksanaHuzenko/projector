#Create Vector class on the 2-d plane ([Optional] n-d plane). Add cross-product method.
class Vector(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def cross_product(self, other):
        return self.x*other.x + self.y*other.y


u = Vector(1, 3)
v = Vector(5, 2)
print(u.cross_product(v))


#Implement the previous method with the magic method
class Vector2(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return self.x*other.x + self.y*other.y


u2 = Vector2(1, 3)
v2 = Vector2(5, 2)

print(v2*u2)


#Create a Robot class with the following attributes: orientation, position_x, position_y. 
#The Robot class should have the following methods: move, turn, and display_position. 
#The move method should take a number of steps and move the robot in the direction it is currently facing. 
#The turn method should take a direction (left or right) and turn the robot in that direction. 
#The display_position method should print the current position of the robot.

class Robot(object):
    def __init__(self):
        self.orientation = [1, 0]
        self.position_x = 0
        self.position_y = 0

    def move(self, steps: int):
        self.position_x += self.orientation[0]*steps
        self.position_y += self.orientation[1]*steps

    def turn(self, direction: str):
        if direction == "left":
            self.orientation = [-self.orientation[1], self.orientation[0]]
        elif direction == "right":
            self.orientation = [self.orientation[1], -self.orientation[0]]
        else:
            print("Wrong input")

    def display_position(self):
        return print(self.position_x, self.position_y)
