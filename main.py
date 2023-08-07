import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkeypress(player.move, "Up")
game_is_on = True
car = CarManager()
scoreboard = Scoreboard()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()
    for cars in car.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.win():
        player.restart_game()
        car.restart_game()
        scoreboard.increase_level()
        scoreboard.show_level()

screen.exitonclick()
