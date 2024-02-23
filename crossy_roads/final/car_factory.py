from turtle import Turtle
import random
from theme import Theme

class CarFactory():

    car_colors = [Theme.dark_purple, Theme.independence, Theme.space_cadet, Theme.tuscany]
    y_height = [-170, -140, -110, -80, -50, -20, 10, 40, 70, 100, 130, 160, 190]

    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_car(self):
        new_car = Turtle("car")
        new_car.penup()
        new_car.color(random.choice(self.car_colors))
        new_car.goto(x = 230, y = random.choice(self.y_height))
        self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += 5