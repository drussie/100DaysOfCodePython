from turtle import Turtle, Screen, pen
import random
import tkinter as tk
from tkinter import messagebox

def show_message(title, message):
    root = tk.Tk()
    root.withdraw()  # Hides the main window
    messagebox.showinfo(title, message)
    root.destroy()

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!",
                            prompt="Which turtle will win the race? Enter your color "
                                   "(red, orange, yellow, green, blue, violet):")
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "violet"]

turtles = []
y_coordinate = -100

for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-230, y_coordinate)
    turtles.append(turtle)
    y_coordinate += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                show_message("Race Result", f"Congratulations! The {winning_turtle} turtle won, and so did you!")
            else:
                show_message("Race Result", f"Sorry! The {winning_turtle} turtle won the race! You bet on {user_bet}.")
            is_race_on = False

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
