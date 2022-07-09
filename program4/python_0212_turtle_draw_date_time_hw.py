import turtle
from datetime import datetime


def draw_number_gap():
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def draw_gap():
    turtle.penup()
    turtle.fd(5)


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
short cut key: 
alt + shift + up   : move block up
alt + shift + down : move block down
ctrl + /           : convert the line to comment
ctrl + d           : compare 2 files (use ctrl key to select 2 files) 
'''

def draw_number(i):

    # 1st stroke - 0 / 1 / 7 not draw
    draw_line(False) if i in [0, 1, 7] else draw_line(True)

    # 2nd stroke - 2 not draw
    draw_line(False) if i == 2 else draw_line(True)

    # 3rd stroke - 1 / 4 / 7 not draw
    draw_line(False) if i in [1, 4, 7] else draw_line(True)

    # 4th stroke - 0 / 2 / 6 / 8 draw
    draw_line(True) if i in [0, 2, 6, 8] else draw_line(False)

    # after 4 strokes, let's the turn the turtle left 90 degree, so that it heads north
    turtle.left(90)

    # 5rd stroke - 1 / 2 / 3 not draw
    draw_line(False) if i in [1, 2, 3] else draw_line(True)

    # 6th stroke - 1 / 4 not draw
    draw_line(False) if i in [1, 4] else draw_line(True)

    # 7th stroke - 5 / 6 not draw
    draw_line(False) if i in [5, 6] else draw_line(True)

    draw_number_gap()






# TEST CODE ----------------------------------------------------

# Step 1) set pen color and size ----------
turtle.color('red')
turtle.pensize(5)
turtle.tracer(0) # turn off animation

# Step 2) Move turtle to the far left -----
turtle.penup()
turtle.back(350)

# Step 3) start draw numbers --------------
'''
HOMEWORK:
With the help of 0210 code, Draw date / time to the turtle console 
'''

now = datetime.now()

# print hour ----------
hour_str = str(now.hour)

if now.hour < 10:
    hour_str = '0' + hour_str

for ch in hour_str:
    draw_number(int(ch))


# print minute ----------
minute_str = str(now.minute)

if now.minute < 10:
    minute_str = '0' + minute_str

for ch in minute_str:
    draw_number(int(ch))


# print second ----------
second_str = str(now.second)

if now.second < 10:
    second_str = '0' + second_str

for ch in second_str:
    draw_number(int(ch))






# Step 4) Finish --------------
turtle.done()