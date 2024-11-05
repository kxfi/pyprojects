#Loops
#For loop, Do something to each individual item

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits: #fruit is a new variable
    print(fruit) #assigns variable fruit to each item in list #Thonny IDE
    #then loops back to beginning and goes to next item
    #in our case we're executing the print statement three times
    print(fruit + " " + "pie") #indentation is inside for loop

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
largest_number = student_scores[0] #or largest_number = 0 
for score in student_scores: #singular in plural
    if score > largest_number:
        largest_number = score
print("The highest score in the class is:", largest_number)
# the loop will continue running until goes through all the scores




phonenumbers = int(input("Phone number "))

final_phone = []
counter = 0
for i in range(phonenumbers):
  final_phone.append(phonenumbers)
  counter += 1
  if counter / 2 == 2 or 4:
    final_phone.append("-")
    counter += 1
print(final_phone)