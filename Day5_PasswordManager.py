import string
import random

# Letters List
az_Letter = string.ascii_letters
letterList = []
for i in az_Letter:
    letterList.append(i)

# Numbers List
numbersList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#Symbols List
symbolsList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']

print("Welcome to the PyPassword Manager!")
letters = int(input("How many letters would you like in your password? \n"))
symbols = int(input("How many symbols would you like? \n"))
numbers = int(input("How many numbers would you like? \n"))


password = []
# Random letters
for i in range(letters):
    letter = random.randint(0, 51)
    password += letterList[letter]
    
# Random numbers
for i in range(numbers):
    num = random.randint(0, 8)
    password += numbersList[num]

# Random symbols
for i in range(symbols):
    sym = random.randint(0, 12)
    password += symbolsList[sym]

random.shuffle(password)
print("Here is your password: " + "".join(password))
