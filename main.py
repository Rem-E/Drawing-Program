import turtle


cursor = turtle.Turtle()
wn = turtle.Screen()



# Window Config
wn.title('Simple Drawing Program by Rem')
wn.bgcolor('black')


# Cursor Config

cursor.color('white')
cursor.shape('square')

# Movement Functions
def cursor_up():
	y = cursor.ycor()
	y += 20
	cursor.sety(y)


def cursor_down():
	y = cursor.ycor()
	y -= 20
	cursor.sety(y)

def cursor_right():
	x = cursor.xcor()
	x += 20
	cursor.setx(x)

def cursor_left():
	x = cursor.xcor()
	x -= 20
	cursor.setx(x)

# Key Functions

def quit_program():
	turtle.bye()




# Toggle Pen up or down

up = False

def pen_up():

    global up
    up = not up
    if up:
        cursor.penup()
    else:
        cursor.pendown()

# Color Cycle via numbers

def color_white():
	cursor.color("white")

def color_green():
	cursor.color ("green")

def color_blue():
	cursor.color("blue")

def color_red():
	cursor.color("red")

def color_yellow():
	cursor.color("yellow")

# Keyboard Bindings 

wn.listen()
wn.onkeypress(cursor_up, "Up")
wn.onkeypress(cursor_down, "Down")
wn.onkeypress(cursor_right, "Right")
wn.onkeypress(cursor_left, "Left")
wn.onkeypress(quit_program, "q")
wn.onkeypress(color_white, "1")
wn.onkeypress(color_green, "2")
wn.onkeypress(color_blue, "3")
wn.onkeypress(color_red, "4")
wn.onkeypress(color_yellow, "5")
wn.onkeypress(pen_up, "e")




turtle.done()