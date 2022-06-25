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

'''
the integer i can be 6 / 8 / 9
'''
def draw_number(i):

    draw_line(True)
    draw_line(True)
    draw_line(True)

    if i == 9:
        draw_line(False)
    elif i == 6 or i == 8:
        draw_line(True)

    turtle.left(90)
    draw_line(True)
    draw_line(True)

    if i == 6:
        draw_line(False)
    elif i == 8 or i == 9:
        draw_line(True)



# TEST CODE ----------------------

# Step 1) set pen color and size ----------
turtle.color('red')
turtle.pensize(5)

# Step 2) Move turtle to the far left -----
turtle.penup()
turtle.back(350)

# Step 3) start draw numbers --------------

draw_number(6)
draw_number_gap()

draw_number(8)
draw_number_gap()

draw_number(9)

turtle.done()


'''
HOMEWORK:
Please make the function draw_number() work for all numbers 0 - 9
'''