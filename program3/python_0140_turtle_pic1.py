import turtle

turtle.color("red", "yellow")

turtle.begin_fill()

for _ in range(50):
    turtle.forward(200)
    turtle.left(170)


turtle.end_fill()

turtle.done()