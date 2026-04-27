from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(15)

def move_backward():
    timmy.backward(15)

def clockwise():
    timmy.right(60)

def anticlockwise():
    timmy.left(30)

def reset_everything():
    timmy.reset()

screen.listen() 
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=anticlockwise)
screen.onkey(key="c", fun=reset_everything)
screen.exitonclick()
