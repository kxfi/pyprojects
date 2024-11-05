#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100 
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")

#33.6 need 0 so formating 
#Data types

#String
#print("Hello"[4]) #the first character is H, programmers start counting from 0 (elecment from string in called Subscript)  

#print("123"+"345") #two strings
 
#Integer   
#print(123+345) #it can be added as just numbers
#123_456_789 the _ is the comma for numbers

#int for whole number
#float for decimal number


#Float, for decimal places, decimal point to float around number

#Boolean to test if something is true or false
#True
#False

# string not int error use type() to check data type or type conversion/casting
# num_char = len(input("What is your name? ")) #num_char is interger data type
# print("Your name is " + str(num_char) + " characters.")

# a = str(123)
# print(type(a))

#mathematical operations 
# 3 + 5
# 7 - 3
# 3 * 2
# print(6/3) #always get a float answer and typer check confirms float answer
# 2 ** 2 #exponent or raise to exponent
#PEMDASLR (Left to right)
# ()
# **
# * / equal importance, calculation left to right
# + - 

# print(3 * (3 + 3) / 3 - 3)

#print(8 / 3) #automatically float so alot of numbers after the decimal point, chops number but 1
#print(round(8 /3)) rounds to whole number
#print(round(8 /3, 2)) rounds to 2 decimal places

#print(4 // 2) #plain number no float

#result = 4 / 2
#result /= 2
#print(result) #such as tracking score, (score +=1 )

# score = 0
# print("your score is " + str(score))
# #or
# score = 0
# height = 1.8
# isWinning = True

# #f-string so no str or int in front, converts for you
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")