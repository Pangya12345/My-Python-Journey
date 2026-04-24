# Import all of the modules and packages
import turtle as t
import random
from turtle import Screen
t.colormode(255)
timmy = t.Turtle()
timmy.shape("arrow")
timmy.speed("fastest")

# Find the random colour level for (Red, Green, Blue)
for i in range (100):
    def random_color():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        timmy.pencolor((r, g, b))
    random_color()
    
# Make turtle draw spinograph
timmy.circle(radius = 50, steps = 20)
timmy.right(7)

# Make the screen appear
screen = Screen()
screen.exitonclick()
