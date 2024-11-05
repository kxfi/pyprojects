from turtle import Turtle, Screen
import time

#screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

startingPositions = [(0,0),(-20,0),(-40,0)]

segments = []

# snake body
for position in startingPositions:
    newSegment = Turtle(shape="square")
    newSegment.color("white")
    newSegment.penup()
    newSegment.goto(position)
    segments.append(newSegment)

# move snake 
gameIsOn = True
while gameIsOn:
    # update screen once all updated
    screen.update()
    # 1 second delay
    time.sleep(1)
    for seg in segments:
        seg.forward(20)
    
    







screen.exitonclick()

