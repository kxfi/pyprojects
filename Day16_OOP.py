# increase in complexity and hard to manage
# break things down
# split tasks into seperate modules
# some modules are reusable (auto car to drone same camera module)

#OOP: split large tasks into small pieces and each piece can be worked on by seperate people and are reusable 
# Example running a restaurant, hire waiter, chef, cleaner, I am manager
#OOP = data + functionality

# Waiter has: holdingplate = True or [4,5,6] (Attributes)
# Waiter (object) does: take order function, take payment function (Methods)
# method a specific object can do (Betty Waiter and Henry Waiter)

# We can generate as much objects a we want with class

'''
from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(100)
tello.rotate_counter_clockwise(90)
tello.move_forward(100)

tello.land()
'''

                   #object #object #Screen class separate class for modularity
from turtle import Turtle, Screen #from turtle.py module import Turtle class and Screen class both
#Object Class()
timmy = Turtle()   # screen is a class in Turtle module
print(timmy)
timmy.shape("turtle")
timmy.color("cyan")
timmy.forward(100)

# ACCESS Attributes
# car.speed   object.attribute
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick() # method

#Example methods: https://docs.python.org/3/library/turtle.html

#Package vs Module
#Package a lot of code bunched together to achieve a goal
# Example pypi for packages can use "table" source code

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

#Access attributes
# changes variable with =, stock align is center 'c'
table.align = "l"
print(table)

# self.car = car can be accessed within class if in the init section