#storing one piece of data a=5
#however, all states, ordering you should think about which are lists
#Lists: fruits = [1, 2, 3, 4]

states_of_america = ["Delaware","Pennsylvania"] #{0,1}
states_of_america[1] = "Pencilvania" #you can alter what's in the list, #-1 or -2 it goes backwards in the list
states_of_america.append("Angelaland") #get added to the end queue append adds to end; theres more datastructures to end
#.extend adds an additional list of states tothe list of states
print(states_of_america) 

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

#index out of range error meaning theres nothing there and beyond 
#when it comes to using big data, let 'len' count and put into variable but add -1 in print to get rid of error:

num_of_states = len(states_of_america)
print(states_of_america [num_of_states - 1])

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", 
"Pears", "Tomatoes", "Celery", "Potatoes"]
#How can we use list to keep in the same container but seperate them out into fruits and vegetables?
#Lists wiithin a list? Nested list!
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"] 
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
    
dirty_dozen = [fruits, vegetables]
print(dirty_dozen) #double brackets shown when print
