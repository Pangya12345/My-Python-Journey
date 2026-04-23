# Import Packages and Random module,./
import colorgram
import turtle as t
from turtle import Screen
import random
# Set up theaspect of the turtle
t.colormode(255)
timmy = t.Turtle()
timmy.shape("arrow")

# Use color from Colorgram
color_list = []
colors = colorgram.extract('hirst.jpg', 10)
for i in range(10):
    color_list.append((colors[i].rgb.r, colors[i].rgb.b, colors[i].rgb.g))

# Set-up the Turtle Position
def set_position():
    timmy.penup()
    timmy.backward(180)
    timmy.right(90)
    timmy.forward(100)
    timmy.left(90)
set_position()

# Set-up the while loop to make it repeat the process 
count = 1
while count <= 10:
    # Set-up the for-loop to paint the dot with 10 dots for each row
    for i in range(10):
        rancolors = random.choice(color_list)
        timmy.pencolor(rancolors)
        timmy.forward(35)
        timmy.dot(20)
    timmy.penup()
    timmy.left(90)
    timmy.forward(35)
    timmy.right(90)
    timmy.backward(350)
    count = count + 1

# Show the run screen
screen = Screen()
screen.exitonclick()


