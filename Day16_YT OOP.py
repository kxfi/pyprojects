# https://www.youtube.com/watch?v=qiSCMNBIP2g
# 
# OOP think about objects and how you can connect them
# https://github.com/damiafuentes/DJITelloPy
# object "=" human 
# attributes data = height, name, etc (defined as variables)
# behavior = talk, dancing, etc (use methods)
# class: blueprint (for phone)
# object: instance (final hard copy phone)
# before creating an object you need a class

'''
from djitellopy import Tello

# object #class
tello = Tello()
      
tello.connect()
tello.takeoff()

      # add variables as parameters so def init(self, ---,---)
tello.move_left(100)
tello.rotate_counter_clockwise(90)
tello.move_forward(100)

tello.land()
'''



# define class
class Computer: # 2 things go in attributes(variables) and behavior(methods=function)
    # special variables _name_ and methods _init_
    def __init__(self, cpu, ram): # initialize variables called AUTOMATICALLY, constructor
        print("in init")
        self.cpu = cpu
        self.ram = ram
        
    # define methods
    def config(self): # self is object that you are passing
        print("Config is", self.cpu, self.ram)
        
# Give com1 a type. com1 is object of computer
# x = 9 ,<class int>, x is object of integer

# object , you can add variables as parameters
# object = design
com1 = Computer('i5', 16) # Object created calls init for you
com2 = Computer('Ryzen', 8)

# To use method use class name and .method name (object name)
com1.config()
com2.config()


