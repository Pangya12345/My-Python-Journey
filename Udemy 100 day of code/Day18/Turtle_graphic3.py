# Import all of the modules and packeges
from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape("turtle")

# Create the colour list and draw the shapes
colour_list = ["red", "blue", "green", "brown", "BlueViolet", "DarkSalmon", "DarkSeaGreen", "DeepPink", "orange", "black", "kiwi"]
number = 2
while number <= 10:
    number = number + 1
    timmy.color(random.choice(colour_list))
    for i in range(number):
        timmy.forward(100)
        timmy.right(360 / number)

# Make the screen appear
screen = Screen()
screen.exitonclick()


