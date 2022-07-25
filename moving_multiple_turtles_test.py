import random
import time
from turtle import Turtle, Screen

class Aliens(Turtle):
    def __init__(self, **kwargs):
        super().__init__()
        self.color(kwargs["color"])
        self.speed("fastest")
        self.penup()
        self.goto(kwargs["xy"])
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=1)  # width 20, height 100, default is 20/20
        self.setheading(270)

        self.alien_dir_x = 1
        self.alien_dir_y = -1
        self.alien_speed_x = 1
        self.alien_speed_y = 20

        self.alien_id = None
        self.alien_x_cor = 0
        self.alien_y_cor = 0
        self.alien_y_cor_list = []
        self.alien_id_list = []
        self.alien_color_list = ["purple","white"]
        self.alien_bullets = []

        self.alien_distance_moved = 0

    def aliens_create(self, width, height):
        # Assign colors & y coord values to each row object
        self.alien_y_cor = height / 2 - 135
        for y in range(0, 8):
            # Change y position of each alien row
            self.alien_y_cor_list.append(self.alien_y_cor)
            self.alien_y_cor = self.alien_y_cor + 30

        # Create 2 rows x 11 aliens
        for row in range(0, 2):
            self.alien_x_cor = -width / 2
            self.alien_y_cor = self.alien_y_cor_list[row]
            # Fit 11 aliens in 1/3 of window width
            for i in range(11):
                # Give every alien a random color
                if i%2==0:
                    color = self.alien_color_list[0]
                else:
                    color = self.alien_color_list[1]
                self.alien_x_cor = self.alien_x_cor + width / 3 / 11

                self.alien_id = Aliens(xy=(self.alien_x_cor, self.alien_y_cor), color=color)
                self.alien_id_list.append(self.alien_id)

    #FINALLY FIXED! SET ABSOLUTE POSITION FOR EVERY SINGLE ALIEN (ONCE A SINGLE ALIEN CROSS BOUNDARY)
    # INSTEAD OF MOVING IT ONE BY ONE & CHANGING ONLY DIRECTION OF MOVEMENT WHICH CAUSES GLITCHES
    def aliens_all_move_x(self):
        for item in range(len(self.alien_id_list)):
            alien_object = self.alien_id_list[item]

            if alien_object.xcor() >= (700 / 2):
                self.alien_dir_x *= -1
                x_dist = + self.alien_speed_x * self.alien_dir_x
                for item in range(len(self.alien_id_list)):
                    self.alien_id_list[item].goto(self.alien_id_list[item].xcor()+x_dist, self.alien_id_list[item].ycor())
            if alien_object.xcor() <= (-700 / 2):
                self.alien_dir_x *= -1
                x_dist = + self.alien_speed_x * self.alien_dir_x
                for item in range(len(self.alien_id_list)):
                    self.alien_id_list[item].goto(self.alien_id_list[item].xcor()+x_dist, self.alien_id_list[item].ycor())
            else:
                x_dist = + self.alien_speed_x * self.alien_dir_x
                for item in range(len(self.alien_id_list)):
                    self.alien_id_list[item].goto(self.alien_id_list[item].xcor()+x_dist, self.alien_id_list[item].ycor())

WIDTH = 700
HEIGHT = 800
screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Space Invaders")
screen.tracer(0)

aliens = Aliens(xy=(0, 0), color="yellow")
aliens.hideturtle()
aliens.aliens_create(WIDTH, HEIGHT)
running = True
while running:
    time.sleep(0.001)
    aliens.aliens_all_move_x()
    screen.update()