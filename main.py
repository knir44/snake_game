import turtle,time
from food import Food
from snake import Snake
from scoreboard import Scoreboard


screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def is_eating():
    food.refresh()
    scoreboard.refresh_score()
    snake.extend()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        is_eating()

    game_is_on = snake.game_over() and snake.self_touching()






screen.clear()
screen.bgcolor("black")
turtle.hideturtle()
turtle.color("white")
style = ('Courier',70,'italic')
turtle.write("Game Over!",font = style,align = 'center')

screen.exitonclick()
