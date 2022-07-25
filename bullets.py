from turtle import Turtle


class Bullets(Turtle):
    def __init__(self, **kwargs):
        super().__init__()
        self.color(kwargs["color"])
        self.shape("turtle")
        self.penup()
        self.direction_y = 1
        self.bullet_speed = kwargs["speed"]
        self.setheading(90)
        self.shapesize(stretch_wid=kwargs["wid"], stretch_len=kwargs["len"])
        try:
            self.x = kwargs["bullet_shot_loc_x"]
            self.y = kwargs["bullet_shot_loc_y"]
        except KeyError:
            self.x = kwargs["bullet_shot_loc_x"]
            self.y = -(800 / 2 - 40)
        self.goto(self.x, self.y)

    # Want bullet to move every main loop frame (want current but not new instance of bullet moving)
    def bullet_move_spaceship(self):
        # print(f"spaceship bullet: {self.x}")
        new_y = self.ycor() + (self.bullet_speed * self.direction_y)
        self.goto(self.x, new_y)

    def bullet_move_alien(self):
        new_y = self.ycor() + self.bullet_speed * (-self.direction_y)
        self.goto(self.x, new_y)