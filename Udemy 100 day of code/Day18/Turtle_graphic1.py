# Import turtle package and screen
from turtle import Turtle, Screen

# Make turtle draw a square
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("orange")
for i in range(4):
    timmy_the_turtle.forward(200)
    timmy_the_turtle.left(90)

# Make the screen appear
screen = Screen()
screen.exitonclick()

