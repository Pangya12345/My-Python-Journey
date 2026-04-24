# Import turtle package and screen
from turtle import Turtle, Screen
pangya = Turtle()
pangya.shape("turtle")

# Make turtle draw a square 
for i in range(50):
    pangya.forward(5)
    pangya.penup()
    pangya.forward(5)
    pangya.pendown()
    pangya.forward(5)

# Make the screen appear
screen = Screen()
screen.exitonclick()