from turtle import Turtle, Screen
from tortoise import Tortoise
from cars import Cars
from scoreboard import Scoreboard
import time

# screen setup
screen = Screen()
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()
# tortoise setup
tortoise = Tortoise()

# cars setup
cars = Cars()

#scoreboard object
scoreboard = Scoreboard()


screen.onkey(tortoise.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    # detect collision with the cars
    for car in cars.all_cars:
        if car.distance(tortoise) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect a successful crossing
    if tortoise.is_at_finish_line():
        tortoise.go_to_start()
        cars.level_up()
        scoreboard.increase_level()



# screen setup -ii
screen.exitonclick()