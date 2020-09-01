import turtle

turtle.setup(200, 100)
t = turtle.Turtle()

t.pencolor("purple")
t.pensize(1)
t.hideturtle()
for i in range(100):
    t.fd(i)
    t.left(100)

turtle.done()
