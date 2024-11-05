# Class is a blueprint for creating an object
# attributes is has, methods is does

class User: # PascalCase
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0 # can change, followers doesn't have to be a parameter
        self.following = 0
        # print("new user being created...")
        
        def follow(self, user):
            user.followers += 1 # user that we're following
            self.following += 1 
        
        
user_1 = User("001", "angela") # create  object
user_2 = User("002", "jack") 

user_1.follow(user_2)

print(user_1.username) # to print you need to print the individual attributes
print(user_1.user_id)

# if user 2 also just use constructor, what should  be initialized first when object is constructed
# you can set variables and counters to they're starting values
# init function always called when you create a new object

# ATTRIBUTES PASS OVER:
class Car:
    def __init__(self, seats):
        self.seats = seats
    
    def enter_race_mode(self):
        self.seats = 2 # Changes 5 to 2  
    
my_car = Car(5) 
print(my_car.seats)