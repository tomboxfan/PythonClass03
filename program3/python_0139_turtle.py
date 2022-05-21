import turtle


for _ in range(4):
    turtle.forward(50)  # walk forward for 50 pixel
    turtle.right(90)    # turn right 90 degree



turtle.penup()
turtle.goto(100, 100)
turtle.pendown()


n = 10
while n <= 40:
    turtle.circle(n)
    n += 10


turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()


turtle.pen(pencolor="purple", fillcolor="orange", pensize=10)

turtle.begin_fill()
turtle.circle(90)
turtle.end_fill()



turtle.done()