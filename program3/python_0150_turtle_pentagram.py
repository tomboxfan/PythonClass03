

import turtle


turtle.pensize(5)
turtle.pencolor('yellow')
turtle.fillcolor('red')


turtle.begin_fill()

for _ in range(5):
    turtle.forward(200)
    turtle.right(144) # HOMEWORK: Why this is 144

turtle.end_fill()


turtle.penup()
turtle.goto(-150, -200)
turtle.color('violet')
turtle.write("Done", font=('Arial', 40, 'normal'))



turtle.done()