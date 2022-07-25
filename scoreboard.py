import time
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.spaceship_rem = 3
        self.score = 0
        self.scoreboard_update()

    def scoreboard_update_end(self,result):
        self.clear()
        self.goto(0, 0)
        if result == "win":
            self.write(f"WAVE CLEARED!! HIGH SCORE: {self.score}", align="center", font=("Consolas", 15 , "normal"))
        if result == "lose":
            self.color("red")
            self.write(f"ALIEN DOMINATION! SCORE: {self.score}", align="center", font=("Consolas", 30 , "normal"))

    def scoreboard_update(self):
        self.clear()
        self.color("white")
        self.goto(-680/2, 380)
        self.write("S", align="center", font=("Consolas", 15 , "normal"))
        self.goto(-680/2, 380-20)
        self.write("P", align="center", font=("Consolas", 15 , "normal"))
        self.goto(-680/2, 380-40)
        self.write("A", align="center", font=("Consolas", 15 , "normal"))
        self.goto(-680/2, 380-60)
        self.write("C", align="center", font=("Consolas", 15 , "normal"))
        self.goto(-680/2, 380-80)
        self.write("E", align="center", font=("Consolas", 15 , "normal"))
        self.goto(-680/2, 380-110)
        self.write("I", align="center", font=("Consolas", 15 , "normal"))
        self.goto(-680/2, 380-130)
        self.write("N", align="center", font=("Consolas", 15 , "normal"))
        self.goto(-680/2, 380-150)
        self.write("V", align="center", font=("Consolas", 15 , "normal"))
        self.goto(-680/2, 380-170)
        self.write("A", align="center", font=("Consolas", 15 , "normal"))
        self.goto(-680/2, 380-190)
        self.write("D", align="center", font=("Consolas", 15 , "normal"))
        self.goto(-680/2, 380-210)
        self.write("E", align="center", font=("Consolas", 15 , "normal"))
        self.goto(-680/2, 380-230)
        self.write("R", align="center", font=("Consolas", 15 , "normal"))
        self.goto(-680/2, 380-250)
        self.write("S", align="center", font=("Consolas", 15 , "normal"))

        self.goto(-640 / 2, 380)
        self.write("S", align="center", font=("Consolas", 15, "normal"))
        self.goto(-640 / 2, 380 - 20)
        self.write("H", align="center", font=("Consolas", 15, "normal"))
        self.goto(-640 / 2, 380 - 40)
        self.write("I", align="center", font=("Consolas", 15, "normal"))
        self.goto(-640 / 2, 380 - 60)
        self.write("P", align="center", font=("Consolas", 15, "normal"))
        self.goto(-640 / 2, 380 - 80)
        self.write("S", align="center", font=("Consolas", 15, "normal"))
        self.goto(-640 / 2, 380 - 110)
        self.write("x", align="center", font=("Consolas", 15, "normal"))

        self.goto(-640 / 2, 380 - 140)
        self.color("green")
        self.write(f"{self.spaceship_rem}", align="center", font=("Consolas", 25 , "bold"))

        self.color("white")
        self.goto(660/2, 760/2)
        self.write("S", align="center", font=("Consolas", 15, "normal"))
        self.goto(660/2, 760/2-20)
        self.write("C", align="center", font=("Consolas", 15, "normal"))
        self.goto(660/2, 760/2-40)
        self.write("O", align="center", font=("Consolas", 15, "normal"))
        self.goto(660/2, 760/2-60)
        self.write("R", align="center", font=("Consolas", 15, "normal"))
        self.goto(660/2, 760/2-80)
        self.write("E", align="center", font=("Consolas", 15, "normal"))

        self.goto(660/2, 760/2-120)
        self.color("green")
        self.write(self.score, align="center", font=("Consolas", 25 , "normal"))

    def score_point(self):
        self.score += 1
        self.scoreboard_update()

    def lose_spaceship(self):
        time.sleep(1)
        self.spaceship_rem-=1
        self.scoreboard_update()
        self.goto(0, 0)
        self.color("white")
        self.write(f"SPACESHIP LOST! {self.spaceship_rem} SHIPS REMAINING", align="center", font=("Consolas", 25, "normal"))
        time.sleep(1)
        self.clear()
        self.scoreboard_update()