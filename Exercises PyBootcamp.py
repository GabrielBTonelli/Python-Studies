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
#