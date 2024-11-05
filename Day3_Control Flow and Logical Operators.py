#conditional statement if/else draw.io for flow charts
# print("Welcome to the rollercoaster! ")
# height = int(input("What is your height in cm? "))  #= sign value to variable

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
    
#== equal to  == check to see value on left equals value to the right
#!= not equal to ! = 

# print("Welcome to the rollercoaster! ")
# height = int(input("What is your height in cm? "))
# bill = 0 #to no restate statments

# if height >= 120:
#      print("You can ride the rollercoaster!") 
#      age = int(input("What is your age?"))
#      if age < 12:  
#          bill = 5#condition 1 if not true then condtion 2
#          print("Child tickets are $5.")           #if condition 2 then do , you can add as many elifs as you want
#      elif age <= 18:                        #if none true then else
#          bill = 7
#          print("Youth tickets are $7.") 
#      else: 
#          bill = 12   #if not less than or equal to 18 or less than 12 then
#          print("Adult tickets are $12.")
#      wants_photo = int(input("Do you want a photo taken? Y or N"))
#      if wants_photo == "Y":
#          bill += 3 #add $3 to their bill. Didn't have to remake variable

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")
         
         
# else:
#      print("Sorry, you have to grow taller before you can ride.")

# if condition1:     if first condition true then do and bypass the rest
#      do A
# elif condition2:
#      do B
# else:
#      do C
#What if situation where you need to check multiple conditions even if previous condition true?
#so multiple ifS
# if all ifs true it'll do 
#3 different sets of if statements "Pizza Order Practice" Day 3

#Logical operators
#Combine conditions with "and"
#both conditions true then true but one condition false then all false

#Combine conditions with "or"
#both statements false then all false 

#not will reverse false condition to true condition

#Love Calculator