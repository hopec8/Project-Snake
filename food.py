from turtle import Turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
SCREEN_LIMIT = 280

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(colors))
        random_x = random.randint(-SCREEN_LIMIT, SCREEN_LIMIT)
        random_y = random.randint(-SCREEN_LIMIT, SCREEN_LIMIT)
        self.goto(random_x, random_y)