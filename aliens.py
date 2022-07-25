from turtle import Turtle
from bullets import Bullets
import random


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
        self.alien_speed_x = 0.2
        self.alien_speed_y = 0.8

        self.alien_id = None
        self.alien_x_cor = 0
        self.alien_y_cor = 0
        self.alien_y_cor_list = []
        self.alien_id_list = []
        self.alien_color_list = ["grey", "brown", "white", "purple"]
        self.alien_bullets = []

        self.alien_distance_moved = 0

    # def alien_difficulty_level(self):
    #     self.aliens_create()
    #     self.alien_speed_x = 10
    #     self.alien_speed_y = 40  # increase speed of aliens
    #     # self.shapesize() #increase size of bullet

    def aliens_create(self, width, height):
        # Assign colors & y coord values to each row object
        self.alien_y_cor = height / 2 - 135
        for y in range(0, 8):
            # Change y position of each alien row
            self.alien_y_cor_list.append(self.alien_y_cor)
            self.alien_y_cor = self.alien_y_cor + 30

        # Create 5 rows x 11 aliens
        for row in range(0, 5):
            self.alien_x_cor = -width / 2
            self.alien_y_cor = self.alien_y_cor_list[row]
            # Fit 11 aliens in 1/3 of window width
            for i in range(11):
                # Give every alien a random color
                color = random.choice(self.alien_color_list)
                self.alien_x_cor = self.alien_x_cor + width / 3 / 11

                self.alien_id = Aliens(xy=(self.alien_x_cor, self.alien_y_cor), color=color)
                self.alien_id_list.append(self.alien_id)

    # ISSUES-- Unintended behaviour: Aliens will randomly move out of position aft a few cycles-- only when flipping; have to readjust x pos?
    # Always the leading turtle causing this weird behaviour
    # Is it boundary check problem or odd window dimension problem
    # leading to turtle moving a few pixels more/less than intended when hitting wall and causing misalignment???
    # First row of turtle doing weird jerk every bounce on wall

    # CANT FIGURE OUT THE CAUSE!!
    # IS IT BECAUSE 1ST ROW HIT RIGHT WALL FIRST; SO IT MOVE LEFT FASTER THAN 2ND ROW DUE TO IT CHANGING DIR WHILE 2ND ROW ISNT;
    # BEFORE 2ND ROW IS CHECKED AND MOVING IN SAME DIR 0.XXX SEC LATER. How to fix?
    # MAKE ALL ALIEN OBJECTS MOVE TOGETHER (IN ONE FRAME #IMPORTANT)
    """    def aliens_move(self, alien_object, xcor, ycor):
            # global WIDTH, HEIGHT
            # print(xcor, ycor)
            new_x = xcor + self.alien_speed_x * self.alien_dir_x
            # new_y = ycor + self.alien_speed_y * self.alien_dir_y
            # print(new_x, ycor)
            alien_object.goto(int(new_x), ycor)
            # print(alien_object.xcor(), alien_object.ycor())
    
            # The aliens begin as five rows of eleven that move left and right as a group,
            # shifting downward each time they reach a screen edge.
            # (BUG: only single turtle that reached edge is shifting; how to make all aliens move?)
            # (FIX: CREATE MOVE ALL FUNCTION)
            if alien_object.xcor() >= 700 / 2:
                # After hit right wall suddenly 1st & 2nd row off by 40x for some reason but why?
                print("HIT RIGHT WALL")
                # print()
                self.alien_dir_x *= -1
                # self.aliens_all_move()
    
            if alien_object.xcor() <= -700 / 2:
                self.alien_dir_x *= -1
                print("HIT LEFT WALL")
                # self.aliens_all_move()"""

    # HOW TO ALLOW ALIEN MOVEMENT INDEPENDENT OF INDIVIDUAL ALIEN?
    # (ACTUALLY ITS UR PREVIOUS ALIEN MOVE FUNCTION)

    # Group of turtles bouncing bet walls bug
    # All aliens should move together in 1 frame; but why still having desync
    # FIX: After 1st leftmost/rightmost turtle hits wall, RESET ALL ALIEN X COORD TO PREDEFINED POSITION?
    # How to change direction of all aliens once one alien hit boundary?
    # Now bug with 1st alien bcos it hit wall first-- become misaligned
    # def aliens_all_move_x(self):
    #     # Shoot missile every 350 x units
    #     # ---but dont want to tie to specific alien otherwise no bullet will be fired if specific alien is eliminated
    #     # ---tie to speed
    #     self.alien_distance_moved += self.alien_speed_x
    #     if self.alien_distance_moved >= 600:
    #         self.aliens_shoot_missile()
    #         self.alien_distance_moved = 0
    #     # FIX?: ADD MAX # OF STEPS EACH ALIEN CAN TAKE??? (800-20)/20=39 ---but alien doesnt move in steps of its own size..
    #     # 1ST ALIEN : 39R; 39-11L
    #     # 2ND ALIEN : 39-1R
    #     # 3RD ALIEN : 39-2R...
    #     # alien_max_steps_L = []
    #     # aliens_max_steps_R = []
    #     # for i in range(39,28,-1):
    #     #     alien_max_steps_L.append()
    #     # for i in range(29,40, 1):
    #     #     aliens_max_steps_R.append()
    #
    #
    #     #Why isn't universal direction variable that applies to every alien working?
    #     for item in range(len(self.alien_id_list)):
    #         alien_object = self.alien_id_list[item]
    #
    #         if alien_object.xcor() >= (700 / 2) or alien_object.xcor() <= (-700 / 2):
    #             self.alien_dir_x *= -1
    #             new_x = alien_object.xcor() + self.alien_speed_x * self.alien_dir_x
    #             alien_object.goto(new_x, alien_object.ycor())
    #         else:
    #             new_x = alien_object.xcor() + self.alien_speed_x * self.alien_dir_x
    #             alien_object.goto(new_x, alien_object.ycor())
    #         # PARTIAL FIX: Reset position of affected aliens; but still cant figure out cause...
    #         # Normal movement until hitting wall
    #         # if -700 / 2 <= self.alien_id_list[0].xcor() <= 700 / 2:
    #         #     # print("Normal movement")
    #         #     new_x = alien_object.xcor() + self.alien_speed_x * self.alien_dir_x
    #         #     alien_object.goto(new_x, alien_object.ycor())
    #
    #         # ONLY CHECK 1ST/LAST ALIENS
    #         # if self.alien_id_list[0].xcor() <= -700 / 2:
    #         #     print("HIT L WALL")
    #         #     for i in range(0, 11):
    #         #         self.alien_dir_x *= -1
    #         #         self.alien_id_list[i].goto(self.alien_id_list[i + 11].xcor(), self.alien_id_list[i].ycor())
    #         #         new_x = alien_object.xcor() + self.alien_speed_x * self.alien_dir_x
    #         #         alien_object.goto(new_x, alien_object.ycor())
    #         #     for x in range(0, len(self.alien_id_list)):
    #         #         alien_object = self.alien_id_list[x]
    #         #         new_x = alien_object.xcor() + self.alien_speed_x * self.alien_dir_x
    #         #         alien_object.goto(new_x, alien_object.ycor())
    #         #
    #         # if self.alien_id_list[10].xcor() >= 700 / 2:
    #         #     print("HIT R WALL")
    #         #     for i in range(0, 11):
    #         #         self.alien_dir_x *= -1
    #         #         self.alien_id_list[i].goto(self.alien_id_list[i + 11].xcor(), self.alien_id_list[i].ycor())
    #         #         new_x = alien_object.xcor() + self.alien_speed_x * self.alien_dir_x
    #         #         alien_object.goto(new_x, alien_object.ycor())
    #         #     for x in range(11, len(self.alien_id_list)):
    #         #         alien_object = self.alien_id_list[x]
    #         #         new_x = alien_object.xcor() + self.alien_speed_x * self.alien_dir_x
    #         #         alien_object.goto(new_x, alien_object.ycor())
    #
    #         # if self.alien_id_list[0].xcor() <= -700 / 2 or self.alien_id_list[54].xcor() >= 700 / 2:
    #         #     self.aliens_all_move_y()

    def aliens_all_move_x(self):
        # Shoot missile every 350 x units
        # ---but dont want to tie to specific alien otherwise no bullet will be fired if specific alien is eliminated
        # ---tie to speed
        self.alien_distance_moved += self.alien_speed_x
        if self.alien_distance_moved >= 9: #RATE OF FIRE
            self.aliens_shoot_missile()
            self.alien_distance_moved = 0

        for item in range(len(self.alien_id_list)):
            alien_object = self.alien_id_list[item]

            if alien_object.xcor() >= (700 / 2):
                self.alien_dir_x *= -1
                self.aliens_all_move_y()
                x_dist = + self.alien_speed_x * self.alien_dir_x
                for item in range(len(self.alien_id_list)):
                    self.alien_id_list[item].goto(self.alien_id_list[item].xcor()+x_dist, self.alien_id_list[item].ycor())
            if alien_object.xcor() <= (-700 / 2):
                self.alien_dir_x *= -1
                self.aliens_all_move_y()
                x_dist = + self.alien_speed_x * self.alien_dir_x
                for item in range(len(self.alien_id_list)):
                    self.alien_id_list[item].goto(self.alien_id_list[item].xcor()+x_dist, self.alien_id_list[item].ycor())
            else:
                x_dist = + self.alien_speed_x * self.alien_dir_x
                for item in range(len(self.alien_id_list)):
                    self.alien_id_list[item].goto(self.alien_id_list[item].xcor()+x_dist, self.alien_id_list[item].ycor())

    def aliens_all_move_y(self):
        for item in range(len(self.alien_id_list)):
            alien_object = self.alien_id_list[item]
            new_y = alien_object.ycor() + self.alien_speed_y * self.alien_dir_y
            # MOVE ALL WITHOUT CONDITION (CONDITION ALREADY PASSED/VALIDATED IN PREVIOUS FUNCTION)
            alien_object.goto(alien_object.xcor(), new_y)

    # Aliens randomly shoot missile every x coords?
    # Want to shoot missile from 1st row of aliens but if 1st row gone; shoot from 2nd row...3rd row... etc
    def aliens_shoot_missile(self):
        # check if index in alien_id_list?
        try:
            for i in range(3):
                random_alien = random.randint(0, 10)
                self.alien_bullets.append(Bullets(bullet_shot_loc_x=self.alien_id_list[random_alien].xcor(),
                                                  bullet_shot_loc_y=self.alien_id_list[random_alien].ycor()-50, color="red",
                                                  wid=0.5, len=3, speed=7))
        except IndexError:
            pass
            # print(random_alien)
            # print(self.alien_id_list[random_alien].xcor())
            # print(self.alien_bullets)
