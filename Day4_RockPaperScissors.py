import random

#let computer choose
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#User input
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
#User wrong input
if user > 2: 
    print("You typed an invalid number, please try again.")
    quit()

#Display images
if user == 0:
    print(rock)
elif user == 1:
    print(paper)
else:
    print(scissors)
    
#computer chooses rock paper or scissors
rock_paper_scissors = [rock, paper, scissors]
computer_choose = random.choice(rock_paper_scissors)

print("Computer chooses: ")

if computer_choose == rock:
    print(rock)
elif computer_choose == paper:
    print(paper)
elif computer_choose == scissors:
    print(scissors)
    

#Rock
if user == 0 and computer_choose == rock:
    print("It's a draw")
    quit()
elif user == 0 and computer_choose == paper:
    print("You lose")
    quit()
elif user == 0 and computer_choose == scissors:
    print("You won")
    quit()
    

if user == 1 and computer_choose == paper:
    print("It's a draw")
    quit()
elif user == 1 and computer_choose == rock:
    print("You won")
    quit()
elif user == 1 and computer_choose == scissors:
    print("You lose")
    quit()

#Scissors
if user == 2 and computer_choose == scissors:
    print("It's a draw")
    quit()
elif user == 2 and computer_choose == rock:
    print("You lose")
    quit()
elif user == 2 and computer_choose == paper:
    print("You won")
    quit()