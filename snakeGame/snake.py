from turtle import Turtle

X_COORDINATE = 0
NUM_SQUARES = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        global X_COORDINATE
        for i in range(NUM_SQUARES):
            self.add_square(X_COORDINATE)
            X_COORDINATE += -20

    def add_square(self, X_COORDINATE):
        new_square = Turtle(shape="square")
        new_square.color('white')
        new_square.penup()
        new_square.goto(X_COORDINATE, 0.0)
        self.squares.append(new_square)

    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def extend(self):
        # Get the position of the last square in the snake
        last_x, last_y = self.squares[-1].position()
        # Extend by placing a new square 20 units left of the last one
        self.add_square(last_x - 20)

    def move(self):
        for square in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square - 1].xcor()
            new_y = self.squares[square - 1].ycor()
            self.squares[square].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)



