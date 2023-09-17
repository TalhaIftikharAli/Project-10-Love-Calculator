# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:02:58 2023

@author: talha.i
"""

# LOVE Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Conversion into lower case:

name1_lower = name1.lower()
name2_lower = name2.lower()

# TRUE and LOVE count:
t = int(name1_lower.count("t")) + int(name2_lower.count("t"))
r = int(name1_lower.count("r")) + int(name2_lower.count("r"))
u = int(name1_lower.count("u")) + int(name2_lower.count("u"))
e = int(name1_lower.count("e")) + int(name2_lower.count("e"))
l = int(name1_lower.count("l")) + int(name2_lower.count("l"))
o = int(name1_lower.count("o")) + int(name2_lower.count("o"))
v = int(name1_lower.count("v")) + int(name2_lower.count("v"))

true = str(t + r + u + e)
love = str(l + o + v + e)

true_love = int(true + love)

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love > 40 and true_love < 50:
    print(f"You score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")