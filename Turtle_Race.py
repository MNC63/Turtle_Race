from turtle import Turtle, Screen
from random import randint

Start_race = False
display = Screen()
display.setup(width = 800, height = 600)

user_choice = display.textinput(title= "Enter your bet: ", prompt ="red, blue, green,...")

if user_choice:
    Start_Race = True
turtle_list = []
distance = 0
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]

for i in range(7):
    Race = Turtle(shape = "turtle")
    Race.color(colors[i])
    Race.penup()
    distance += 75
    Race.goto(-380,-300 + distance)
    turtle_list.append(Race)

while Start_Race:
    for turtle_each in turtle_list:
        if turtle_each.xcor() > 370:
            Start_Race = False
            wining_clor = turtle_each.pencolor()
            if wining_clor == user_choice:
                print(f"You Win")
            else:
                print(f"You Lose, ", f"{wining_clor} is the winner")
        turtle_each.forward(randint(1, 10))

display.exitonclick()