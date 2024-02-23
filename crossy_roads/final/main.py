# turtle — Turtle graphics
# https://docs.python.org/3/library/turtle.html#module-turtle#

import time
from turtle import Screen
from theme import Theme
from player import Player
from car_factory import CarFactory
from scoreboard import Scoreboard

# Setup Screen
canvas = Screen()
canvas.setup(width = 500, height = 500)
canvas.title("Go, Toni, go!")
canvas.bgcolor(Theme.almond)
canvas.register_shape("car", ((0,0),(20,0),(20,-30),(10,-40),(0,-30)))
canvas.tracer(0) # turn animation off

# Initialization
toni = Player()
car_factory = CarFactory()
scoreboard = Scoreboard()

is_game_on = True
counter = 0

canvas.listen()
canvas.onkey(toni.move, "Up")

while is_game_on:
    counter += 1

    time.sleep(0.1) 
    canvas.update() # Getting the screen to update every 0.1 seconds. To be used because tracer was turned off in ln 16.

    if counter % 5 == 0: # generates a new car only every 5th time the game loop runs
        car_factory.create_car()

    car_factory.move_cars()

    # Toni successfully crossing the line
    if toni.cross_finish_line():
        toni.goto_start()
        car_factory.increase_speed()
        scoreboard.increase_level()

    # Toni the Turtle collides with car
    for car in car_factory.all_cars:
        if car.distance(toni) < 25: # less than 25 px from the center of the car
            is_game_on = False # exit loop
            scoreboard.game_over()

canvas.exitonclick()