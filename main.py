# Assignment: Space Invaders
"""Build the classic arcade game where you shoot down alien ships."""
"""
Using Python Turtle, build the classic shoot 'em up game - space invaders game.

Space Invaders Wikipedia Page
https://en.wikipedia.org/wiki/Space_Invaders
Your space ship can move left and right and it can hit some alien ships. Every second the aliens will move closer to your ship. 
Once the aliens touch your ship then it's game over. 
There are usually some barriers between you and the aliens which offers you defensive positions.

You can play the game here:
https://elgoog.im/space-invaders/
"""
"""
Space Invaders is a fixed shooter in which the player moves a laser cannon horizontally across the bottom of the screen and fires at aliens overhead. 
The aliens begin as five rows of eleven that move left and right as a group, 
shifting downward each time they reach a screen edge. 
The goal is to eliminate all of the aliens by shooting them. 

While the player has three lives, the game ends immediately if the invaders reach the bottom of the screen. 
The aliens attempt to destroy the player's cannon by firing projectiles. 
The laser cannon is partially protected by stationary defense bunkers 
which are gradually destroyed from the top by the aliens and, if the player fires when beneath one, the bottom.

As aliens are defeated, their movement and the game's music both speed up. 
Defeating all the aliens brings another wave which starts lower, a loop which can continue endlessly. 
A special "mystery ship" will occasionally move across the top of the screen and award bonus points if destroyed.
"""
# Approach
"""
1. Create all objects--- spaceship, aliens (5 rows x 11)(x16? multiples), bullets
   >> turtle custom shapes? #turtle.register_shape
2. Create defensive barriers --- shape of own choice (but disintegrates upon bullet collision)
3. Movement --- spaceship (left right event listener), aliens (fixed pattern), bullets (straight y)
4. Bullet impact --- remove spaceship/alien upon bullet impact  (collision bet bullet - spaceship/alien)
5. Win/lose condition --- all aliens eliminated/all lives lost
6. MULTIPLE WAVES #Bonus (get the basics working first)
"""
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from spaceship import Spaceship
from aliens import Aliens
import time
from bullets import Bullets
from spaceobstacles import SpaceObstacles

WIDTH = 700
HEIGHT = 800
screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Space Invaders")
# screen.register_shape("spaceship.gif")

screen.tracer(0)

scoreboard = Scoreboard()
# --------------CREATING SPACESHIP--------------------------------#
spaceship = Spaceship((-15, -(HEIGHT / 2 - 30)))

# --------------CREATING SPACE OBSTACLES--------------------------------#
spaceobstacles = SpaceObstacles(xy=(0, 0))
spaceobstacles.hideturtle() #Hide middle block -- wont detect for collision
spaceobstacles.space_blocks()

# --------------CREATING ALIENS--------------------------------#
aliens = Aliens(xy=(0, 0), color="yellow")
aliens.hideturtle()
aliens.aliens_create(WIDTH, HEIGHT)

# python keyboard key names
screen.listen()
screen.onkey(spaceship.left_m, "Left")
screen.onkey(spaceship.right_m, "Right")
screen.onkey(spaceship.shoot_missile, "space")

# scoreboard.spaceship_rem = 3
alien_hits = 0
bullet_hits = 0
running = True
while running:
    time.sleep(0.001)
    screen.update()
    aliens.aliens_all_move_x()


    for i in range(len(aliens.alien_bullets)):
        bullet_hits = 0
        try:
            aliens.alien_bullets[i].bullet_move_alien()
        except IndexError:
            continue
        # Check for missile collision with space obstacles (bef spaceship)
        try:
            #do check for all missiles with all space obstacles
            for j in range(len(spaceobstacles.block_space)):
                if aliens.alien_bullets[i].distance(spaceobstacles.block_space[j]) < 20:
                    print("SpaceObstacle hit!")
                    #Why are missiles passing through obstacles? Might be referring to the wrong object
                    aliens.alien_bullets[i].hideturtle() #Why missiles not removed & stuck on screen? #Oh hide first then remove; otherwise object not found
                    aliens.alien_bullets.remove(aliens.alien_bullets[i])

                    spaceobstacles.block_space[j].hideturtle()
                    spaceobstacles.block_space.remove(spaceobstacles.block_space[j])
        except IndexError:
            continue

        # Check for missile collision with spaceship
        if aliens.alien_bullets[i].distance(spaceship) < 20:
            print("Spaceship shot!")
            print(f"scoreboard.spaceship_rem bef: {scoreboard.spaceship_rem}")
            for item in aliens.alien_bullets:
                item.hideturtle()
            aliens.alien_bullets.clear()

            bullet_hits += 1

            # Only want to deduct max 1 life each loop - even with multiple bullet hits
            # But still have multiple hits per frame bcos missile didnt disappear fast enough
            # Have to delete/reset missile position instead of just hiding?
            if bullet_hits == 1:
                # scoreboard.spaceship_rem -= 1
                print(f"scoreboard.spaceship_rem aft: {scoreboard.spaceship_rem}")
                scoreboard.lose_spaceship()
                spaceship.reset_spaceship()
            if scoreboard.spaceship_rem == 0:
                print("SPACESHIP SUPPLY DEPLETED!")
                result = "lose"
                scoreboard.scoreboard_update_end(result)
                running = False

    try:
        spaceship.move_missile()
        spaceship.check_intervals+=1
        spaceship.missile_cooldown()
    except IndexError:
        continue
    for i in range(len(spaceship.bullets)):
    # Check for spaceship missile collision with space obstacles
        try:
            # do check for all missiles with all space obstacles
            for k in range(len(spaceobstacles.block_space)):
                if spaceship.bullets[i].distance(spaceobstacles.block_space[k]) < 20:
                    print("SpaceObstacle hit!")
                    # Why are missiles passing through obstacles? Might be referring to the wrong object
                    spaceship.bullets[
                        i].hideturtle()  # Why missiles not removed & stuck on screen? #Oh hide first then remove; otherwise object not found
                    spaceship.bullets.remove(spaceship.bullets[i])
                    spaceship.active_missiles.remove(spaceship.active_missiles[i])
                    spaceship.current_missile_shot = 0
                    spaceship.move_missile()

                    spaceobstacles.block_space[k].hideturtle()
                    spaceobstacles.block_space.remove(spaceobstacles.block_space[k])
        except IndexError:
            continue
        try:
            #CAUSES GLITCH IN ALIEN MOVEMENT BCOS UR ALIEN MOVEMENT DEPENDS ON SPECIFIC ALIENS.
            # AFT REMOVING SUDDENLY ALIENS CANT MOVE ANYMORE


            # Check for spaceship missile collision with aliens
            for j in range(len(aliens.alien_id_list)):
                for i in range(len(spaceship.bullets)):
                    if spaceship.bullets[i].distance(aliens.alien_id_list[j]) < 20:
                        alien_hits += 1
                        print(alien_hits)
                        scoreboard.score_point()
                        aliens.alien_id_list[j].hideturtle()
                        aliens.alien_id_list.remove(aliens.alien_id_list[j])
                        spaceship.bullets[i].hideturtle()
                        spaceship.bullets.remove(spaceship.bullets[i])
                        spaceship.active_missiles.remove(spaceship.active_missiles[i])
                        spaceship.current_missile_shot = 0
                        spaceship.move_missile()

        except IndexError:
            continue
    if len(aliens.alien_id_list) == 0:
        print("WAVE CLEARED!")
        result = "win"
        scoreboard.scoreboard_update_end(result)
        running = False
    # MOVES ALL ALIENS
    # Solving issue: Aliens will randomly move out of position aft a few cycles

    # aliens_x_cor_1strow = []
    # aliens_x_cor_2ndrow = []

    # print(f"# of aliens: {len(aliens.alien_id_list)}")
    # print(aliens.alien_id_list[21])
    # BUGFIX- CHECKING 12th ALIEN OBJECT (Anomaly)
    # for item in range(0, 11):
    #     alien_object = aliens.alien_id_list[item]
    #     aliens.aliens_move(alien_object, alien_object.xcor(), alien_object.ycor())
    #     aliens_x_cor_1strow.append(alien_object.xcor())
    # for item in range(11, 22):  # (FIXED) 11-22 INSTEAD OF 12-23 Weird! Why 2nd row controlling 1st alien of 3rd row??
    #     alien_object = aliens.alien_id_list[item]
    #     aliens.aliens_move(alien_object, alien_object.xcor(), alien_object.ycor())
    #     aliens_x_cor_2ndrow.append(alien_object.xcor())
    #
    # if item == 10 and alien_object.xcor() >= 680 / 2:
    #     print(item, alien_object.xcor())
    #     print(21, aliens.alien_id_list[21].xcor())
    # if item == 21 and alien_object.xcor() >= 680 / 2:
    #     print(10, aliens.alien_id_list[10].xcor())
    #     print(item, alien_object.xcor())
    # if item == 0 and alien_object.xcor() <= -680 / 2:
    #     print(item, alien_object.xcor())
    #     print(11, aliens.alien_id_list[11].xcor())
    # if item == 11 and alien_object.xcor() <= -680 / 2:
    #     print(0, aliens.alien_id_list[0].xcor())
    #     print(item, alien_object.xcor())
    #     # print(item)
    #     # print(alien_object.xcor(),alien_object.ycor())
    # print(f"1st: {aliens_x_cor_1strow}")
    # print(len(aliens_x_cor_1strow))
    # print(f"2nd: {aliens_x_cor_2ndrow}")
    # print(len(aliens_x_cor_2ndrow))

    # for item in aliens.alien_id_list:
    #     print(item)
    #     aliens.aliens_move(item, item.xcor(), item.ycor())

screen.exitonclick()
