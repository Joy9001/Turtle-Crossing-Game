import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Create a player
user = Player()
screen.onkeypress(user.move_up, "Up")
screen.onkeypress(user.move_right, "Right")
screen.onkeypress(user.move_left, "Left")

# Create Random Cars
car_manager = CarManager()

# Create a scoreboard
score_board = Scoreboard()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect Collision with the cars
    for car in car_manager.cars:
        if user.distance(car) < 20:
            game_on = False
            score_board.game_over()

    # Detect when turtle reaches the other side
    if user.is_at_finish_line():
        user.go_to_start()
        car_manager.level_up()
        score_board.level += 1
        score_board.update_scoreboard()

screen.exitonclick()
