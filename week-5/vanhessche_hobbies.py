# Title: vanhessche_hobbies.py
# Author:  John Vanhessche
# Date:  17 November 2022
# Description:  Exercise 5.3

# adding the random module
import random

# List of hobbies and days
hobbies = ["computers", "cycling", "gaming", "cooking", "puzzles"];
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

# iterating through hobbies, and printing on the console.
for x in hobbies:
    print(x);    

# Iterating through the days.  Though not in the instructions, am randomizing a hobby and adding to the message.
for x in days:
    y = random.choice(hobbies);   
    if x == "Saturday" or x == "Sunday":
        print("It's " + x + ", you are off and should enjoy your " + y + ".");
    else:
        print(x + " is a work day.")
