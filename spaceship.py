from turtle import Turtle
from bullets import Bullets
import time


class Spaceship(Turtle):
    def __init__(self, xy):
        super().__init__()
        self.color("green")
        self.penup()
        self.goto(xy)
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(0)
        self.check_intervals = 0
        self.bullet_cooldown = 0
        self.bullets = []
        self.active_missiles = []
        self.current_missile_shot = 0

    def reset_spaceship(self):
        self.goto((-15, -(800 / 2 - 30)))

    def left_m(self):
        self.setheading(0)
        self.backward(5)

    def right_m(self):
        self.setheading(0)
        self.forward(5)

    # How to move missile shot by spaceship? OH!!! Seperate missile creation and movement then call in main loop
    # Limit max # of missiles/ missile cooldown ?
    # (Check # of bullets on screen (using position of each)/ length of bullet list)
    def shoot_missile(self):
        # --------------CREATING BULLETS--------------------------------#
        # print("Missile Fired!")

        # Only allow missile fire if theres <3 missiles on screen currently (<5 missiles too easy to clear all aliens)
        if self.current_missile_shot < 3 and len(self.active_missiles) < 3 and self.bullet_cooldown <= 0:
            # print(f"SPACESHIP X LOCATION: {self.xcor()}")
            self.current_missile_shot += 1
            # print(f"Missiles shot: {self.current_missile_shot}")
            self.bullets.append(Bullets(bullet_shot_loc_x=self.xcor(), color="green", wid=0.4, len=1, speed=5))
            # How to set cooldown for bullet without pausing whole game loop?
            self.bullet_cooldown = 0.2  # want 0.2 sec cd bet bullets. loop checked every 0.001 sec
            #Weird that the cooldown time interval is not indicative of real time interval
            # (esp with diff amount of objects created)
        else:
            print(f"CANNOT FIRE! BULLET COOLDOWN: {self.bullet_cooldown}")

    def missile_cooldown(self):
        if self.check_intervals == 0.1/0.001/10: #acts like a timer #want to check every 0.1 sec? 0.1/0.001 but takes 10x more time for check proc
        # Reduce bullet cooldown every frame, if no bullets left reset cd to 0
        # Problem; multiple instances of bullet will continue bullet cooldown timer
        # SOLUTION: CHECK IN DIFFERENT FUNCTION INSTEAD OF move_missile; CHECK EVERY X MAIN LOOPS
            self.bullet_cooldown -= 0.1
            self.check_intervals = 0
            print(self.bullet_cooldown)

    # Bug: Shot missile stops moving once new missile shot concurrently
    # Create new instance of bullet instead of referring to same instance
    def move_missile(self):
        # if len(self.bullets) == 0:
        #     self.bullet_cooldown = 0
        for i in range(len(self.bullets)):


            # Take note of # of bullets currently on screen
            # Remove bullets already off screen, if not total count doesnt increase
            # Update bullet X position every frame; and add new bullet to self.active_missiles if not created before
            try:
                self.active_missiles[i] = self.bullets[i].ycor()
            except IndexError:
                self.active_missiles.append(self.bullets[i].ycor())
            self.bullets[i].bullet_move_spaceship()

        try:
            # print(f"bef remove # of active missiles: {len(self.active_missiles)}")
            for missile in range(len(self.active_missiles)):
                if self.active_missiles[missile] > (800 / 2):
                    # print(f"y_cor to remove: {self.active_missiles[missile]}")
                    # BUG AFTER REMOVING MISSILE, WILL BE REPLACED IN ABOVE FOR LOOP WITH bullet[i]
                    self.active_missiles.pop(missile)
                    # print("Active missile removed!")
                    # print(self.active_missiles)
                    if self.current_missile_shot > 0:
                        self.current_missile_shot -= 1
        except IndexError:
            pass
            # print("NO MISSILES LEFT; SHOULD = 0")
            # print(self.active_missiles)
        try:
            for missile in range(len(self.bullets)):
                # print(f"bullet removal : {self.bullets[missile].ycor()}")
                if self.bullets[missile].ycor() > (2000 / 2):
                    self.bullets.pop(missile)
        except IndexError:
            pass
            # print("NO BULLETS LEFT; SHOULD = 0")
            # print(self.bullets)

        # print(f"# of bullets /len(self.bullets)= {len(self.bullets)}")
        # print(f"Active missile locations /self.active_missiles: {self.active_missiles}")
        # print(f"# of active missiles /len(self.active_missiles): {len(self.active_missiles)}")
        # print(f"Missiles remaining /self.current_missile_shot: {self.current_missile_shot}\n")
