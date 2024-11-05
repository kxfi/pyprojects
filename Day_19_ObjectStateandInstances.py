from turtle import Turtle, Screen
import random

isRaceOn = False
screen = Screen()
screen.setup(width = 500, height = 400) 
userBet = screen.textinput(title="Make your bet", prompt ="Which turtle will win the race? Enter a color: ")
positions = [-90, -60, -30, 0, 30, 60]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
allTurtles = []

for turtle_index in range(0,6):
    newTurtle = Turtle()
    newTurtle.shape("turtle")
    newTurtle.color(colors[turtle_index])
    newTurtle.penup() 
    newTurtle.goto(x=-230,y=positions[turtle_index])
    allTurtles.append(newTurtle)
    
# when user makes 
if userBet:
    isRaceOn = True

while isRaceOn:
    for turtle in allTurtles:
        if turtle.xcor() > 230: #An if statement with changing while condition stops loop
            isRaceOn = False
            winningColor = turtle.pencolor()
            if winningColor == userBet:
                print(f"You've won! The {winningColor} turtle is the winner!")
            else:
                print(f"You've lost! The {winningColor} turtle is the winner!")
        randomDistance = random.randint(0, 10)
        turtle.forward(randomDistance)


screen.exitonclick()