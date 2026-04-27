from turtle import Turtle, Screen
import random as r 

random_colour = ["purple", "blue", "green", "yellow", "orange", "red", "pink"]
random_position_set_up = [0, 50,  -50, 100, -100,  150, -150]
    
for i in range(7):
    timmy = Turtle()
    timmy.shape("turtle")
    colour = r.choice(random_colour)
    timmy.color(colour)
    random_colour.remove(colour)
    timmy.penup()
    timmy.backward(950)                 
    timmy.right(90)
    random_position = r.choice(random_position_set_up)
    timmy.forward(random_position)
    random_position_set_up.remove(random_position)
    timmy.left(90)







    

screen = Screen()
screen.setup(width = 2000, height = 1000)
user_bet = screen.textinput(title = "Turtle racing Game!", prompt = "Enter a color")
screen.exitonclick()

