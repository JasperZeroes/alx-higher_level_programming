#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    remainder = number % 10
else:
    remainder = number % -10

if remainder > 5:
    print(f"Last digit of {number} is {remainder} and is greater than 5")
elif remainder < 6 and remainder != 0:
    print(f"Last digit of {number} is {remainder} and is < 6 and ! 0")
else:
    print(f"Last digit of {number} is {remainder} and is 0")
