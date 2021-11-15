import turtle
import winsound
window = turtle.Screen()
window.title("Pong by @6Waifu9")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)



# Score
score_1 = 0
score_2 = 0



# Player 1
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("blue")
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)



# Player 2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("red")
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(350, 0)



# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2



# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write ("Blue: 0  Red: 0" , align="center" ,font=("Courier", 24, "normal"))

# Functions
def player_1_up():
    y = player_1.ycor()
    y += 20
    player_1.sety(y)

def player_1_down():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)

def player_2_up():
    y = player_2.ycor()
    y += 20
    player_2.sety(y)

def player_2_down():
    y = player_2.ycor()
    y -= 20
    player_2.sety(y)
    
# keyboard binding
window.listen()
window.onkeypress(player_1_up, "w")
window.onkeypress(player_1_down, "s")
window.onkeypress(player_2_up, "Up")
window.onkeypress(player_2_down, "Down")


# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounch.wav", winsound.SND_ASYNC)


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounch.wav", winsound.SND_ASYNC)

        


    if ball.xcor()> 390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score_1 +=1
        pen.clear()
        pen.write ("Blue: {}   Red: {}".format(score_1, score_2) , align="center" ,font=("Courier", 24, "normal"))
        winsound.PlaySound("puntscore.wav", winsound.SND_ASYNC)


    if ball.xcor() < -390:
       ball.goto(0 , 0)
       ball.dx *= -1
       score_2 +=1
       pen.clear()
       pen.write ("Blue: {}  Red: {}".format(score_1, score_2), align="center" ,font=("Courier", 24, "normal"))
       winsound.PlaySound("puntscore.wav", winsound.SND_ASYNC)



    
    # Player and ball aanraken
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_2.ycor() + 50 and ball.ycor() > player_2.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounch.wav", winsound.SND_ASYNC)

    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_1.ycor() + 50 and ball.ycor() > player_1.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounch.wav", winsound.SND_ASYNC)
