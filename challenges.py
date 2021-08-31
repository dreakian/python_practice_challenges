############################################################################################
##############################     THE BASICS     ##########################################
############################################################################################

# #Challenge 1

# user_first_name = input("Enter your first name: ")
# # print(f"Hello, {user_first_name}.")

# #Challenge 2

# user_surname = input("Enter your surname: ")
# print(f"Hello, {user_first_name} {user_surname}.")

# Challenge 3

# print("What do you call a bear with no teeth? \n A gummy bear!")

# Challenge 4

# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))
# answer = first_number + second_number
# print(f"The total is {answer}.")

# Challenge 5

# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))
# third_number = int(input("Enter the third number: "))
# answer = (first_number + second_number) * third_number
# print(f"The total is {answer}.")

# Challenge 6

# slices_pizza_started = int(input("How many slices of pizza did you start with?: "))
# slices_pizza_eaten = int(input("How many slices of pizza have you eaten?: "))
# slices_pizza_left = slices_pizza_started - slices_pizza_eaten
# print(f"\nYou have {slices_pizza_left} slices of pizza left.")

# Challenge 7

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# new_age = age + 1
# print(f"{name} next birthday you will be {new_age}.")

# Challenge 8

# total_bill = float(input("Enter the total price of the bill: $"))
# number_of_diners = int(input("Enter how many diners attended: "))
# payment_per_diner = total_bill / number_of_diners
# print(f"\nEach person must pay ${payment_per_diner}.")

# Challenge 9

# number_of_days = int(input("Enter number of days: "))
# hours_in_numbers_of_days = number_of_days * 24
# minutes_in_numbers_of_days = number_of_days * 1440
# seconds_in_numbers_of_days = number_of_days * 86400
#
# print(f"""
# In {number_of_days} day(s), there are:
#     {hours_in_numbers_of_days} hours.
#     {minutes_in_numbers_of_days} minutes.
#     {seconds_in_numbers_of_days} seconds.
# """)

# Challenge 10

# weight_in_kilograms = float(input("Enter a weight: "))
# weight_in_pounds = 2.204 * weight_in_kilograms
# print(f"{weight_in_kilograms} kilograms is {weight_in_pounds} pounds.")

# Challenge 11

# first_number = int(input("Enter a number that is greater than 100: "))
# second_number = int(input("Enter a number that is less than 10: "))
# difference = first_number / second_number
#
# print(f"""
# The number {second_number} goes into the number {first_number}:
#
# {difference} times.
# """)

############################################################################################
##############################     IF STATEMENTS   #########################################
############################################################################################

# Challenge 12

# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))
#
# if first_number > second_number:
#     print(f"\nThe second number: {second_number} \nThe first number: {first_number}")
# elif second_number > first_number:
#     print(f"\nThe first number: {first_number} \nThe second number: {second_number}")

# Challenge 13

# number = int(input("Enter a number less than 20: "))
#
# if number >= 20:
#     print("\nToo high")
# else:
#     print("\nThank you.")

# Challenge 14

# number = int(input("Enter a number between 10 and 20: "))
#
# if 10 <= number <= 20:
#     print("\nThank you")
# else:
#     print("\nIncorrect answer")

# Challenge 15

# color = input("What is your favorite color?: ")
#
# if color == "red":
#     print("I like red too")
# elif color == "RED":
#     print("I like red too")
# elif color == "Red":
#     print("I like red too")
# else:
#     print(f"I don't like {color}, I prefer red")

# Challenge 16

# is_raining_question = input("Is it raining? Yes/No: ").lower()
#
# if is_raining_question == "yes":
#     is_windy_question = input("\nIs it windy? Yes/No: ").lower()
#     if is_windy_question == "yes":
#         print("\nIt is too windy for an umbrella")
#     elif is_windy_question == "no":
#         print("\nTake an umbrella")
# elif is_raining_question == "no":
#     print("\nEnjoy your day")

# Challenge 17
#
# age = int(input("Enter your age: "))
#
# if age >= 18:
#     print("\nYou can vote")
# elif age == 17:
#     print("\nYou can learn to drive")
# elif age == 16:
#     print("\nYou can buy a lottery ticket")
# elif age < 16:
#     print("\nYou can go Trick-or-Treating")

# Challenge 18

# number = int(input("Enter a number: "))
#
# if number < 10:
#     print("Too low")
# elif 10 <= number <= 20:
#     print("Correct")
# elif number > 20:
#     print("Too high")

# Challenge 19

# user_request = input("Enter a number: 1, 2 or 3: ")
#
# if user_request == str(1):
#     print("\nThank you")
# elif user_request == str(2):
#     print("\n Well done")
# elif user_request == str(3):
#     print("\nCorrect")
# else:
#     print("\nError message")

############################################################################################
################                 STRINGS AND NUMBERS AS VARIABLES             ##############
############################################################################################

# Challenge 20
#
# first_name = input("Enter your first name: ")
# length_first_name = len(first_name)
# print(f"The length of {first_name} is {length_first_name}")

# Challenge 21

# first_name = input("Enter your first name: ")
# surname = input("Enter your surname: ")
#
# whole_name = first_name + " " + surname
# length_whole_name = len(whole_name) - 1
# print(f"\nThe length of {whole_name}, excluding the space is {length_whole_name}")

# Challenge 22
#
# first_name = input("Enter your first name: ").lower()
# surname = input("Enter your surname: ").lower()
#
# whole_name = (first_name + " " + surname).title()
# print(whole_name)

# Challenge 23

# Twinkle, twinkle, little star

#
# nursery_rhyme = input("Enter the first line of a nursery rhyme: \n")
# length_nursery_rhyme = len(nursery_rhyme)
# print(length_nursery_rhyme)
#
# starting_number = int(input("Enter a number between 0 and 29: "))
# ending_number = int(input("Enter a number between 0 and 29: "))
#
# print(f"\n{nursery_rhyme[starting_number:ending_number]}")

# Challenge 24

# word = input("Enter any word: ")
# print(word.upper())

# Challenge 25

# first_name = input("Enter your first name: ")
#
# if len(first_name) < 5:
#     surname = input("Enter your surname: ")
#     whole_name = first_name + surname
#     print(f"{whole_name.upper()}")
# elif len(first_name) >= 5:
#     print(f"{first_name.lower()}")

# Challenge 26

# if word starts with consonant, take that starting consonant letter and put it at the end of the word and then add -ay

# if word starts with a vowel, take that starting vowel letter and put it at the end of the word and then add -way

# word = input("Enter a word: ").lower()
# starting_letter = word[0]
# pig_latin_word_if_starting_letter_is_vowel = word + "way"
# pig_latin_word_if_starting_letter_is_consonant = word[1:] + starting_letter + "ay"
#
# if starting_letter == "a":
#     print(f"""
#     Normal word: {word}
#
#     Pig Latin word: {pig_latin_word_if_starting_letter_is_vowel}
#     """)
# elif starting_letter == "e":
#     print(f"""
#     Normal word: {word}
#
#     Pig Latin word: {pig_latin_word_if_starting_letter_is_vowel}
#     """)
# elif starting_letter == "i":
#     print(f"""
#     Normal word: {word}
#
#     Pig Latin word: {pig_latin_word_if_starting_letter_is_vowel}
#     """)
# elif starting_letter == "o":
#     print(f"""
#     Normal word: {word}
#
#     Pig Latin word: {pig_latin_word_if_starting_letter_is_vowel}
#     """)
# elif starting_letter == "u":
#     print(f"""
#     Normal word: {word}
#
#     Pig Latin word: {pig_latin_word_if_starting_letter_is_vowel}
#     """)
# elif starting_letter == "y":
#     print(f"""
#     Normal word: {word}
#
#     Pig Latin word: {pig_latin_word_if_starting_letter_is_vowel}
#     """)
# else:
#     print(f"""
#     Normal word: {word}
#
#     Pig Latin word: {pig_latin_word_if_starting_letter_is_consonant}
#     """)

############################################################################################
###########################                 MATHS             ##############################
############################################################################################

# Challenge 27

# decimal_number = float(input("Enter a number with many decimals, i.e: 2.23423423424: "))
# print(decimal_number*2)

# Challenge 28
#
# decimal_number = float(input("Enter a number with many decimals, i.e: 2.23423423424: "))
# double_decimal_number = decimal_number * 2
# print(round(double_decimal_number, 2))

# Challenge 29
#
# import math as m
#
# number = int(input("Enter a number that is greater than 500: "))
#
# number_square_root = m.sqrt(number)
# print(round(number_square_root, 2))

# Challenge 30

# import math as m
#
# pi = m.pi
# print(pi)
# format_pi = "{:.5f}".format(pi)
# print(format_pi)

# Challenge 31

# import math as m
#
# pi = m.pi
# circle_radius = float(input("Enter the radius of a circle: "))
#
# area_of_circle = pi * (circle_radius * circle_radius)
# print(round(area_of_circle, 2))

# Challenge 32

# import math as m
#
# pi = m.pi
# cylinder_radius = float(input("Enter the radius of a cylinder: "))
# cylinder_depth = float(input("Enter the depth of a cylinder: "))
#
# area_of_cylinder = pi * (cylinder_radius * cylinder_radius)
# volume_of_cylinder = area_of_cylinder * cylinder_depth
# format_volume_of_cylinder = "{:.3f}".format(volume_of_cylinder)
#
# print(format_volume_of_cylinder)

# Challenge 33

# import math as m
#
# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))
#
# division = first_number / second_number
# floor_division = m.floor(division)
# remainder = first_number % second_number
#
# print(f"{first_number} divided by {second_number} is {floor_division} with {remainder} remaining")

# Challenge 34

# print(f"""
# 1) Square
# 2) Triangle
# """)
#
# number = input("Enter a number: ")
#
# if number == str(1):
#     length_of_square = float(input("Enter the length of the side of the square: "))
#     area_of_square = length_of_square * length_of_square
#     print(f"{area_of_square}")
# elif number == str(2):
#     base_of_triangle = float(input("Enter the base of the triangle: "))
#     height_of_triangle = float(input("Enter the height of the triangle: "))
#     area_of_triangle = (base_of_triangle * height_of_triangle) / 2
#     print(f"{area_of_triangle}")
# else:
#     print("\nYou did not make a valid selection")


############################################################################################
###########################                 FOR LOOPS         ##############################
############################################################################################

# Challenge 35

# name = input("Enter your name: ")
#
# for i in range(3):
#     print(name)

# Challenge 36

# name = input("Enter your name: ")
# number = int(input("Enter a number: "))
#
# for i in range(number):
#     print(name)

# Challenge 37

# name = input("Enter your name: ")
#
# for letter in name:
#     print(letter)

# Challenge 38

# name = input("Enter your name: ")
# number = int(input("Enter a number: "))
#
# for letter in name:
#     for i in range(number):
#         print(letter)

# Challenge 39

# number = int(input("Enter a number between 1 and 12: "))
#
# for x in range(13):
#     print(x * number)

# Challenge 40

# number = int(input("Enter a number below 50: "))
#
# for count in range(51 - number):
#     print(50 - count)

# Challenge 41
#
# name = input("Enter your name: ")
# number = int(input("Enter a number: "))
#
# if number < 10:
#     for i in range(number):
#         print(name)
# elif number > 10:
#     for i in range(3):
#         print("Too high")

# Challenge 42

# total = 0
#
# for i in range(5):
#     number = int(input("\nEnter a number: "))
#     include_number = input(f"Do you want to include this number: {number}? Yes/No: ").lower()
#
#     if include_number == "yes":
#         total += number
#
#     elif include_number == "no":
#         total = total
#
# print(f"\nThe total number is {total}")

# Challenge 43

# count_direction = input("\nWhich direction do you want to count?: Up/Down: ").lower()
#
# if count_direction == "up":
#     top_number = int(input("\nWhat is the top number?: "))
#     for count in range(top_number + 1):
#         print(f"{count}")
# elif count_direction == "down":
#     number = int(input("Enter a number below 20: "))
#     for count in range(20 - number + 1):
#         print(f"{20 - count}")
# else:
#     print("\nI don't understand")

# Challenge 44
#
# people_to_invite = int(input("How many people do you want to invite to the party?: "))
#
# if people_to_invite < 10:
#     for count in range(people_to_invite):
#         name = input("\nEnter a person's name: ")
#         print(f"\n{name} has been invited")
# elif people_to_invite >= 10:
#     print("\nToo many people")

############################################################################################
###########################             WHILE LOOPS           ##############################
############################################################################################

# Challenge 45
#
# total = 0
#
# while total <= 50:
#     number = int(input("Enter a number: "))
#     total += number
#     print(f"The total is {total}")

# Challenge 46

# condition = True
#
# while condition:
#     number = int(input("Enter a number: "))
#     if number < 5:
#         number
#     elif number > 5:
#         print(f"\nThe last number you entered was a {number}")
#         condition = False

# Challenge 47

# total = 0
#
# first_number = int(input("Enter the first number: "))
# second_number = int(input("Enter the second number: "))
# new_total = first_number + second_number
#
# continue_adding = input("Do you want to continue adding numbers: Y/N: ").lower()
#
# while continue_adding == "y":
#     first_number = int(input("\nEnter the first number: "))
#     second_number = int(input("Enter the second number: "))
#     new_total += first_number + second_number
#
#     continue_adding = input("\nDo you want to continue adding numbers: Y/N: ").lower()
#
# if continue_adding == 'n':
#     total += new_total
#     print(total)

# Challenge 48

# count = 0
#
# name = input("Enter a name: ")
# print(f"{name} has now been invited")
# count += 1
#
# continue_inviting = input("Do you want to continue inviting people to your party?: Y/N: ").lower()
#
# while continue_inviting == "y":
#     name = input("\nEnter a name: ")
#     print(f"{name} has now been invited")
#     count += 1
#     continue_inviting = input("\nDo you want to continue inviting people to your party?: Y/N: ").lower()
#
# if continue_inviting == "n":
#     if count == 1:
#         print(f"\n{count} person is coming to the party")
#     elif count > 1:
#         print(f"\n{count} people are coming to the party")


# Challenge 49

# compnum = 50
# count = 0
#
# number = int(input("Enter a number: "))
#
# while number != compnum:
#     if number < compnum:
#         print("Guess is too low")
#         count += 1
#         number = int(input("\nEnter a number: "))
#     elif number > compnum:
#         print("Guess is too high")
#         count += 1
#         number = int(input("\nEnter a number: "))
#
# if number == compnum:
#     print(f"\nWell done, you took {count} attempts")


# Challenge 50

# number = int(input("Enter a number between 10 and 20: "))
#
# while number < 10 or number > 20:
#     if number < 10:
#         print("\nToo low")
#         number = int(input("Enter a number between 10 and 20: "))
#     elif number > 20:
#         print("\nToo high")
#         number = int(input("Enter a number between 10 and 20: "))
#
# if 10 <= number <= 20:
#     print("\nThank you")

# Challenge 51

# num = 10
# condition = None
# changed_num = num - 1
#
# print(f"There are {num} green bottles hanging on the wall, {num} green bottles hanging on the wall,"
#       f"and if 1 green bottle should accidentally fall...")
# question = int(input("How many green bottles will be hanging on the wall?: "))
#
# while changed_num != 0 and question == changed_num:
#     print(f"There will be {changed_num} green bottles hanging on the wall, "
#           f"{changed_num} green bottles hanging on the wall,"
#           f"and if 1 green bottle should accidentally fall...")
#     question = int(input("\nHow many green bottles will be hanging on the wall?: "))
#     changed_num = changed_num - 1
#
# if question != changed_num:
#     print("No, try again")
#
# elif changed_num == 0:
#     print("\nThere are no more green bottles hanging on the wall")

############################################################################################
##############################          RANDOM           ###################################
############################################################################################

# Challenge 52

# import random as r
#
# print(r.randint(1, 100))

# Challenge 53
#
# import random as r
#
# fruit_list = ["Orange", "Apple", "Strawberry", "Banana", "Peach"]
#
# print(r.choice(fruit_list))

# Challenge 54

# import random as r
#
# options = ["h", "t"]
#
# computer_choice = r.choice(options)
#
# user_choice = input("Choose heads or tails: H/T: ").lower()
#
# if user_choice == computer_choice:
#     print("You win")
# elif user_choice != computer_choice:
#     print("Bad luck")
#
# print(f"Computer selected: {computer_choice}")

# Challenge 55
#
# import random as r
#
# random_choice = r.randint(1, 5)
# print(random_choice)
#
# user_choice = int(input("Choose a number between 1 and 5: "))
#
# if user_choice == random_choice:
#     print("Well done")
# elif user_choice < random_choice:
#     print("Too low")
#     user_choice_second = int(input("\nChoose another number between 1 and 5: "))
#     if user_choice_second == random_choice:
#         print("Correct")
#     else:
#         print("You lose")
# elif user_choice > random_choice:
#     print("Too high")
#     user_choice_second = int(input("\nChoose another number between 1 and 5: "))
#     if user_choice_second == random_choice:
#         print("Correct")
#     else:
#         print("You lose")

# Challenge 56

# import random as r
#
# random_choice = r.randint(1, 10)
# print(random_choice)
#
# user_choice = int(input("Enter a number: "))
#
# while user_choice != random_choice:
#     user_choice = int(input("Enter a number: "))


# Challenge 57

# import random as r
#
# random_choice = r.randint(1, 10)
# print(random_choice)
#
# user_choice = int(input("Enter a number: "))
#
# while user_choice != random_choice:
#     if user_choice < random_choice:
#         print("Too low")
#         user_choice = int(input("Enter a number: "))
#     elif user_choice > random_choice:
#         print("Too high")
#         user_choice = int(input("Enter a number: "))

# Challenge 58

# import random as r
#
# number_of_questions = 5
# score = 0
# count = 0
#
# while count != 5:
#     num1 = r.randint(0, 100)
#     num2 = r.randint(0, 100)
#     answer = num1 + num2
#     user_answer = int(input(f"\nWhat is {num1} + {num2}?: "))
#
#     if user_answer == answer:
#         score += 1
#         count += 1
#     elif user_answer != answer:
#         score = score
#         count += 1
#
# print(f"\nYou got {score} out of {number_of_questions} correct")

# Challenge 59

# import random as r
#
# colors = ["red", "yellow", "blue", "green", "purple"]
# random_color = r.choice(colors)
#
# print(colors)
# user_choice = input("\nPick a color from the list above: ").lower()
#
# while user_choice != random_color:
#     if random_color == colors[0]:
#         print("\nI bet you're RED with anger")
#         user_choice = input("Pick a color from the list above: ")
#     elif random_color == colors[1]:
#         print("\nI bet you're YELLOW with shame")
#         user_choice = input("Pick a color from the list above: ")
#     elif random_color == colors[2]:
#         print("\nYou are probably feeling BLUE right now")
#         user_choice = input("Pick a color from the list above: ")
#     elif random_color == colors[3]:
#         print("\nI bet you are GREEN with envy")
#         user_choice = input("Pick a color from the list above: ")
#     elif random_color == colors[4]:
#         print("\nI bet you're PURPLE with confusion")
#         user_choice = input("Pick a color from the list above: ")
#
# if user_choice == random_color:
#     print("\nWell done")

############################################################################################
##############################        TURTLE GRAPHICS           ############################
############################################################################################

# Challenge 60
