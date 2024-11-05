#Random module
import random
import Day4_my_module

# # random_integer = random.randint(1, 10)
# # print(random_integer)

print(Day4_my_module.pi)

#module: cant see whats going on in large piece of code
#each module is responsible for a different bit of functionality of your program
#helps with collaboration so people can work on different things
#python made random module so we dont have to worry about the math

#To make a module make new py file my_module.py, code "pi = 3.141592653589"
#you can import my_module.py from file by import my_module.py

#floating number
# random_float = random.random() #between 0 and 1
# print(random_float)

# random_float = 5 * random.random() #between 0 and 5 expand range by multiplying and not including 5
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")