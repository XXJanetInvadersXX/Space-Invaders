# Space Invaders
# Set up the screen
# Python3.7 Windows
import turtle
import math
import random
from PIL import Image


# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
turtle.screensize(1280, 720)
wn.bgpic("background.gif")

turtle.register_shape("KUK.gif")
turtle.register_shape("BÖGHORAN.gif")

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()

# Set score
score = 0

# Draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" % score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

# Player Movement
playerspeed = 15

# Enemies (Basic)
Number_of_enemies = 5
# Lists
enemies = []

# add enimies to lists
for i in range(Number_of_enemies):
    enemies.append(turtle.Turtle())


# Lists
enemies = []

# add enimies to lists
for i in range(Number_of_enemies):
    enemies.append(turtle.Turtle())

Number_of_enemies = 3

for enemy in enemies:
    enemy.color("red")
    enemy.shape("triangle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

for enemy in enemies:
    enemy.color("red")
    enemy.shape("BÖGHORAN.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)


enemyspeed = 2


# The bullet
bullet = turtle.Turtle()
bullet.penup()
bullet.goto(0, 1000)
bullet.color("yellow")
bullet.shape("KUK.gif")
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()


bulletspeed = 20

# Define Bullet state
# ready - ready to fire
# fire - Bullet is firing
bulletstate = "ready"

# Move the player left and right


def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    # Declare bulletstate
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # move the bullet above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    ext = math.pow(t1.ycor() - t2.ycor(), 2)
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + ext)
    if distance < 15:
        return True
    else:
        return False


# Create keyboard bindings
wn.listen()
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")
wn.onkey(fire_bullet, "space")

yeet = bool

# Main game loop
while yeet:
    for enemy in enemies:
        # move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move the enemy back and forward
        if enemy.xcor() > 280:
            # move down all enemies
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                # change direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

            # Check collision
        if isCollision(bullet, enemy):
            # reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)

            # reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)

            # Update score
            score += 10
            scorestring = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check the bullet is on the top
    if bullet.ycor() > 275:
        if bulletstate == 'fire':
            bullet.hideturtle()
            bulletstate = "ready"

    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        print("Game Over")
        break


wn.mainloop()
