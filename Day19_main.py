from turtle import Turtle, Screen

# Turtle event listeners
# user input, listen method
    
# function when key triggered
# function as an input
# def calculator (n1,n2, func)
# result = calculator(2, 3, divide) which is higher order function

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
    
def move_backwards():
    tim.backward(10)
    
def turn_left():
    tim.left(10)
    
def turn_right():
    tim.right(10)
    
def clear_drawing():
    tim.clear() 
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards) 
screen.onkey(key="s", fun=move_backwards) 
screen.onkey(key="a", fun=turn_left) 
screen.onkey(key="d", fun=turn_right) 
screen.onkey(key="c", fun=clear_drawing) 

screen.exitonclick()



