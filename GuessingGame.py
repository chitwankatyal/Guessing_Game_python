# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:47:48 2021

@author: chitwan
Guessing game
"""
import random
low_num = 0
high_num = 20
secret_number = random.randint(low_num, high_num)
guess_limit = 5
guess_counter = 0
counter = 1

user_name = (input("\nEnter your name: "))
print(f"\nWelcome to the Guessing Game {user_name}")

while guess_counter < guess_limit:
    print("Please choose a number between 0 and 20")
    guess = int(input(f"\nPlease enter your {counter}st guess: "))
    counter += 1
    guess_counter += 1
  
    if guess < secret_number:
      print(f"\nThe guess {guess} is too low. Try again!")
    elif guess > secret_number:
      print(f"\nThe guess {guess} is too high. Try again!")
    else:
      print(f"\nYour guess {guess} is correct.Congratulations!!")
      break

if guess_counter == guess_limit:
    print("Sorry! You have used all your attempts. Better luck next time.")
    

  
    



