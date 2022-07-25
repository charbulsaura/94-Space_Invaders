from turtle import Turtle
import random


class SpaceObstacles(Turtle):
    def __init__(self, **kwargs):
        super().__init__()
        self.color("grey")
        self.speed("fastest")
        self.penup()
        self.goto(kwargs["xy"])
        self.shape("circle")
        self.multiplier = [0.3,0.5,0.7,0.9,1.1,1.3,1.5,1.7]
        self.shapesize(stretch_wid=random.choice(self.multiplier), stretch_len=random.choice(self.multiplier))  # width 20, height 100, default is 20/20
        self.setheading(270)

        self.block_x_cor = 0
        self.block_y_cor = 0
        self.space_blocker = None
        self.block_space = []

    def space_blocks(self):
        # Random Shapes in random locations (x200 blocks) -- too many
        for blocks in range(0, 120):
            self.block_x_cor = random.randint(-350,350)
            self.block_y_cor = -random.randint(1,int(500 / 2))
            self.space_blocker = SpaceObstacles(xy=(self.block_x_cor, self.block_y_cor))
            self.block_space.append(self.space_blocker)


# import time
# from turtle import Turtle, Screen
#
# WIDTH = 700
# HEIGHT = 800
# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=WIDTH, height=HEIGHT)
# screen.title("Space Invaders")
#
# s = SpaceObstacles(xy=(0, 0))
# s.space_blocks()
#
# running = True
# while running:
#     time.sleep(0.001)
#     screen.update()
# screen.exitonclick()
