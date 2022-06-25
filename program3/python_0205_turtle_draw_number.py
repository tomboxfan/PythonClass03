'''
requirement: Use turtle to draw today's date.
'''

'''
Analysis:
2022-06-25
'''

import turtle



def draw_number_gap():
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def draw_gap():
    turtle.penup()
    turtle.fd(5)

'''
For certain numbers, sometimes, the line is not drawn. But the turtle still needs to walk the way.
Because of this, we need another boolean param - draw.
When it is True, pen down.
When it is False, pen up.
'''

def draw_line(draw):
    draw_gap()

    if draw:
        turtle.pendown()
    else:
        turtle.penup()

    turtle.fd(40)
    draw_gap()
    turtle.right(90)




def draw_number_6():
    draw_line(True)
    draw_line(True)
    draw_line(True)
    draw_line(True)

    turtle.left(90)
    draw_line(True)
    draw_line(True)
    draw_line(False)


def draw_number_8():
    draw_line(True)
    draw_line(True)
    draw_line(True)
    draw_line(True)

    turtle.left(90)
    draw_line(True)
    draw_line(True)
    draw_line(True)


def draw_number_9():
    draw_line(True)
    draw_line(True)
    draw_line(True)
    draw_line(False)

    turtle.left(90)
    draw_line(True)
    draw_line(True)
    draw_line(True)




# TEST CODE ----------------------

turtle.color('red')
turtle.pensize(5)



draw_number_6()

draw_number_gap()


draw_number_8()

draw_number_gap()


draw_number_9()



turtle.done()