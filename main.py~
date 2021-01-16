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



# Keyboard Bindings 

wn.listen()
wn.onkeypress(cursor_up, "Up")
wn.onkeypress(cursor_down, "Down")
wn.onkeypress(cursor_right, "Right")
wn.onkeypress(cursor_left, "Left")




turtle.done()