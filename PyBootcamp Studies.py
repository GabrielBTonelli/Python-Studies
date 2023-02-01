#----------------------------------------------Day two

# two_digit_number = input("Type a two digit number: ")
# convert = str(two_digit_number)
# soma = (int(convert[0]) + int(convert[1]))
# print(soma)
# ______________________________________________________________________________________________________


#_______________________________________________________________________________________________________BMI Calculator

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
#
# altura = float(height)
# peso = float(weight)
# BMI = (peso / (altura * altura))
#
# print(int(BMI))
# _______________________________________________________


#-------------------------------------------------------- How many Years, Weeks and Months do you still have in Earth?
# age = input("What is your current age?")
#
# age_as_int = int(age)
# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12
#
# print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
# -------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------TIP CALCULATOR
# print("Hello, there! Try this tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? "))
# people = int(input("How many people to split the bill?"))
#
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
#
# print(f"Each person should pay: {final_amount}")
# --------------------------------------------------------------------------------------------------
#
#
# -------------------------------------------------------------------------------------------------ODD OR EVEN NUMBERS
#number = int(input("Which number do you want to check? "))
#
#if number % 2 == 0:
#    print(f"Your number is {number} and it's an EVEN NUMBER!")
#else:
#    print(f"{number} is an ODD NUMBER!")
#---------------------------------------------------------------------------------------------------------
#
#---------------------------------------------------------------------------------------------------------BMI Calculator
#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))
#
#bmi = round(weight / (height * height))
#
#if bmi < 18.5:
#    print(f"Your BMI is {bmi}, you are underweight.")
#elif bmi < 25:
#    print(f"Your BMI is {bmi}, you have a normal weight.")
#elif bmi < 30:
#    print(f"Your BMI is {bmi}, you are slightly overweight.")
#elif bmi < 35:
#    print(f"Your BMI is {bmi}, you are obese.")
#else:
#    print(f"Your BMI is {bmi}, you are clinically obese.")
#_____________________________________________________________________________________________________
#
#-----------------------------------------------------------------------------------------------------Is it a leap year?
#
#year = int(input("Which year do you want to check? "))
#
#if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#    print("Leap year.")
#else:
#    print("Not leap year.")
#---------------------------------------------------------------------------------------
#
#----------------------------------------------------------------------------------------------DAY FOUR
#                                 RANDOMISATION
#
# it's a module and you have to import it to use with: 
# import random
#
# ex.: random_interger = random.randit(1, 10)
#     print(random_interger)
#
# you'll get a different random number between 1 and 10 every time you run it.
#
# randomFloat = random.random() * 5
#
# ex.: love_score = random.randint(1, 100)
#      print(f"Your love score is {love_score}.")



#                                     LIST  []

# ex.: fruits = [item1, item2]
# print(fruits[1]) == item2

# to change an item's name in the list:
# fruits[1] = "apple"

# to add a single item to the end of the list:
# fruits.append("item3")

# to add more than one item to the list:
# fruits.extend(["item3", "item4"])


# EXERCISE: MAKE A RANDOM LIST OF WHO IS GOING TO PAY THE MEAL.
# 
# import random
# 
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# num_items = len(names)

# random_choice = random.randint(0, num_items - 1)
# chosenone = names[random_choice]

# print(chosenone + "is going to buy the meal today!")
#___________________________________________________________________________________

#--------------------------------------------------------------------------------------Python Loops

#fruits = ["Apple", "Peach", "Pear"]
#for fruit in fruits:
#    print(fruit)
#    print(fruit + " Pie")

# ONE OF THE MOST ASKED QUESTIONS ON INTERVIEWS #
#total = 0
#for number in range (2, 101, 2):
#    total += number
#print(total)

#----------------------------------FIZZBUZZ
#number = 0
#for number in range (1, 101):
#    if number % 3 == 0 and number % 5 ==0:
#        print("FizzBuzz")
#    elif number % 5 == 0:
#        print("Buzz")
#    elif number % 3 == 0:
#        print ("Fizz")
#    else:
#        print(number)

#-------------------------------------------------------------Exercise CHECKING THE STUDENTS' HEIGHT:

#student_heights = input("Input a list of student heights: ").split()
#for n in range(0, len(student_heights)):
#  student_heights[n] = int(student_heights[n])

#total_height = 0
#for height in student_heights:
#    total_height += height

#number_of_students = 0
#for student in student_heights:
#    number_of_students += 1

#average_student_heigh = total_height / number_of_students
#print(round(average_student_heigh))
#-----------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------HIGHEST SCORE EXCERCISE

#student_scores = input("Input a list of student scores ").split()
#for n in range(0, len(student_scores)):
#  student_scores[n] = int(student_scores[n])
#print(student_scores)

#highest_score = 0
#for score in student_scores:
#    if score > highest_score:
#        highest_score = score

#print(f"The highest score in the class is: {highest_score}")
#----------------------------------------------------------------------------------------------------

#---------------------PYPASSWORD GENERATOR----------------------------------#
#
#import random
#letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
#'t', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#password_list = []

#print("Welcome to the Password Generator!")

#num_letters = int(input("How many letters would you like in your password?\n"))
#num_symbols = int(input("How many symbols would you like?\n"))
#num_numbers = int(input("How many numbers would you like?\n"))


#for char in range(1, num_letters + 1):
#    password_list.append(random.choice(letters))
    

#for char in range(1, num_symbols + 1):
#    password_list.append(random.choice(symbols))

#for char in range(1, num_numbers + 1):
#    password_list.append(random.choice(numbers))

#rand_list = random.shuffle(password_list)

#password = "".join(rand_list)

#print(f"Your password is: {password}")
#---------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------WHILE LOOP

# while something_is_true:
#     do this
#     then do this
#     then do this

# you also can use WHILE or WHILE NOT to check the truth of the situation and limit the loop


#--------------------------------------------------------------------------FUNCTIONS AND INPUTS

# Arguments & Parameters

# on the CAESAR CIPHER excercise you can learn how to turn a loop repeatly picking "yes/no" and also you can
# learn how to program harder!
#________________________________________________________________________________________________________________________________








#------------------------------------------------DICTIONARIES IN PYTHON----------------------------------------------------------

#To create your dictionary in Python the sintaxy it's like {key: value} than you substitute for what do you want.
#Exemple:
# {key: value}
# {"Bug": "an error in a program that prevents the program from running as expected"}

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again."

#     }

# if you want to call one of the items from a diccionary, you'll use:
# print(programming_dictionary["Bug"])


#_______________________________________________adding new items to dictionary.
# programming_dictionary["Key"] = "Value"
# print(programming_dictionary)

# one method often used in programming is to create an empty dictionary and insert the values on it with previous teach.
#_______________________________________________create an empty dictionary:
# empty_dictionary = {}
# empty_dictionary[]

#_______________________________________________wipe an existing dictionary
# often used due an program which needs to start over again with an empty dictionary.
# programming_dictionary = {}
# print(programming_dictionary)

#_______________________________________________Edit an item in a dictionary
# programming_dictionary["Bug"] = "NEW VALUE"

#_______________________________________________Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# #-------------------------------------------------------------------EXERCISE CHANGING SCORE TO GRADES
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
        
# print(student_grades)
#________________________________________________________________________________________________________

#______________________________________________NESTING (Put one inside the other)
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

#---------------------------------------nesting a list in a dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

#---------------------------------------nesting dictionary in a dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_not_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 0}
# }

#---------------------------------------nesting a dictionary in a list
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_not_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 0
#     }
# ]

# #______________________________________Write the function that will allow new countries to be added to the travel_log. 👇
# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)






#____________________________________________________________________________________Day 10: FUNCTIONS WITH OUTPUTS

#---------------------------------------this function can give you the captalised Name.
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "you didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"  # the RETURN works as the end of the function. Nothing happens after this!

# print(format_name(input("What is your first name? "), input("What's your last name? ")))


#-------------------------------------------------------------------------------------DOCSTRINGS
# create definitions for the functions that we write
# it has to go after the first line after our DECLARATION

# def format_name(f_name, l_name):
#     """This function can give you the captalised name and last name."""
#     if f_name == "" or l_name == "":
#         return "you didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"  # the RETURN works as the end of the function. Nothing happens after this!

# print(format_name(input("What is your first name? "), input("What's your last name? ")))
