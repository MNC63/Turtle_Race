from turtle import Turtle, Screen
from random import randint


display = Screen()
display.setup(width = 800, height = 600)

# #display textinput("Enter your bet: ", "Turtle color")
# user_choice = display.textinput(title= "Enter your bet: ", prompt ="red, blue, green,...")
# print(user_choice)

distance = 0
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]

for i in range(7):
    Race = Turtle(shape = "turtle")
    Race.color(colors[i])
    Race.penup()
    distance += 75
    Race.goto(-380,-300 + distance)

display.exitonclick()