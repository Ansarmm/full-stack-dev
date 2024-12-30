budget = int(input("Enter your budget (in dollars): ")) #User enter budget
if budget <= 20: #If budget more than 20, user can go to the forest or beach
    print("You can go to the forest or beach") 
elif budget > 20 and budget < 50: #If budget between 20 and 50, user can go to the forest, beach, desert or hotel
    print("You can go to the forest, beach, desert or hotel")
elif budget > 50: #If budget more than 50, user can go to the forest, beach, desert, hotel, mountains or SPA
    print('You can go to the forest, beach, desert, hotel, mountains or SPA')
else:
    print("Error: enter number") #Error if user enter incorrect number
print("You prefer active or relaxing holiday? Enter 1 if active, 2 if relaxing") #Choice for active or relaxing holidays
choice = input("Your choice: ")
if choice == "1":
    print("Where do you want to go for an active holiday?") #Choices for active holidays
    print("Enter 1 for mountains, 2 for forest and 3 for desert")
    active_choice = input("Your choice: ")
    if active_choice == "1":
        print("You have chosen mountains, don`t forget first-aid kit!")
    elif active_choice == "2":
        print("You have chosen forest, don`t forget compass!")
    elif active_choice == "3":
        print("You have chosen desert, don`t forget water!")
    else:
        print("Error: pelase, enter number from 1 to 3")
elif choice == "2":
    print("Where do you want to go for relaxing holiday?") #Choices for relaxing holidays
    print("Enter 1 for beach, 2 for SPA, 3 for hotel")
    relaxing_choice = input("Your choice: ")
    if relaxing_choice == "1":
        print("You have chosen beach, don`t forget your sunscreen!")
    elif relaxing_choice == "2":
        print("You have chosen SPA, have a good rest!")
    elif relaxing_choice == "3":
        print("You have chosen hotel, have a good rest!")
    else:
        print("Error: please, enter nubmer from 1 to 3")    
else:
    print("Error: please, enter number from 1 to 2")