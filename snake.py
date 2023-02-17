import turtle as t
from turtle import Screen

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
DIRECTION = {"Up":90,"Down":270,"Right":0,"Left":180}


class Snake:
    def __init__(self):
        self.list_snakes = []
        for position in STARTING_POSITIONS:
           self.add_segment(position)

        self.head = self.list_snakes[0]
        self.head.color("red")


    def add_segment(self,position):
        new_snake = t.Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.list_snakes.append(new_snake)

    def extend(self):
        self.add_segment(self.list_snakes[-1].position())

    def turn_one_by_one(self):
        size_of_list_snakes = len(self.list_snakes) - 1
        for index in range(size_of_list_snakes, 0, -1):
            new_x = self.list_snakes[index - 1].xcor()
            new_y = self.list_snakes[index - 1].ycor()
            self.list_snakes[index].goto(new_x, new_y)


    def self_touching(self):
        for each_snake in self.list_snakes[1:]:
                if self.head.distance(each_snake) < 15:

                    return False
        return True

    def move(self):
        self.turn_one_by_one()
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTION["Down"]:
            self.head.setheading(DIRECTION["Up"])


    def down(self):
        if self.head.heading() != DIRECTION["Up"]:
            self.head.setheading(DIRECTION["Down"])


    def right(self):
        if self.head.heading() != DIRECTION["Left"]:
             self.head.setheading(DIRECTION["Right"])

    def left(self):
        if self.head.heading() != DIRECTION["Right"]:
             self.head.setheading(DIRECTION["Left"])


    def game_over(self):

        if self.head.xcor() > 280 or self.head.xcor() < -280:

            return False

        elif self.head.ycor() > 280 or self.head.ycor() < -280:
            return False

        return True