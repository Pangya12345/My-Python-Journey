from turtle import Turtle, Screen
import random as r 

random_colour = ["purple", "blue", "green", "yellow", "orange", "red", "pink"]
random_position_set_up = [0, 50, -50, 100, -100, -150, 150]
random_movement = r.randint(10, 30)

all_turtle = []
for i in range(7):
    timmy = Turtle()
    color = r.choice(random_colour)
    timmy.color(color)
    timmy.shape("turtle")
    timmy.penup()
    timmy.backward(480)
    timmy.left(90)
    random_direction = r.choice(random_position_set_up)
    timmy.forward(random_direction)
    timmy.right(90)
    random_colour.remove(color)
    random_position_set_up.remove(random_direction)
    all_turtle.append(timmy)



screen = Screen()
screen.setup(width = 500, height = 1000)
user_bet = screen.textinput(title = "Turtle racing Game!", prompt = "Enter a color")
screen.exitonclick()

