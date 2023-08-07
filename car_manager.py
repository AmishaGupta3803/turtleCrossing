from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_no = random.randint(1,6)
        if random_no == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def move(self):
        for cars in self.all_cars:
            cars.forward(self.move_distance)

    def restart_game(self):
        self.move_distance += MOVE_INCREMENT
