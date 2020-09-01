import turtle
import math
import random

speed = 1
depth = 0.00


class RainDrop:
    def __init__(self):
        pass

    def fall(self, start_x, start_y, depth):
        drop = turtle.Turtle(visible=False)
        drop.color('purple')
        drop.hideturtle()
        drop.up()
        drop.goto(start_x, 0)
        drop.right(90)
        drop.pensize(depth)
        drop.pendown()
        drop.forward(depth * 3)


r = RainDrop()
for i in range(10):
    r.fall(random.randint(0, 100), random.randint(5, 15), random.randint(2, 10))

turtle.done()
