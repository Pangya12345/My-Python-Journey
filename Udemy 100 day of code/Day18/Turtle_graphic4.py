# Import all of the module and packages
import turtle as t
from turtle import Screen
import random
timmy = t.Turtle()
timmy.shape("arrow")
action_list = ["turn right", "turn left", "forward", "backward"]
for i in range(100000000000000000000):
    t.colormode(255)

# Find the random colour level for (Red, Green, Blue)
    def random_color():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        timmy.pencolor((r, g, b))
    random_color()

# Make turtle move in the random path and paint inthe random colour
    timmy.speed(8)
    timmy.pensize(8)
    action = random.choice(action_list)
    if action == "turn right":
        timmy.right(90)
    elif action == "turn left":
        timmy.left(90)
    elif action == "forward":
        timmy.forward(10)
    else:
        timmy.backward(10)

# Make the screen appear
screen = Screen()
screen.exitonclick()
