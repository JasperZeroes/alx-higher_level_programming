#!/bin/python3
'''
while True:
    try:
        x = float(input("Enter a number you want to divide : "))
        print("First instruction passed")
        y = float(input("Enter the divisor : "))
        print("Second instruction passed.")
        quotient = x/y
        print("The quotient is", quotient)
        break
    except ZeroDivisionError as ZeroDivisionError:
        print("Try again. Error due to : {0}".format(ZeroDivisionError))
    except ValueError as ValError:
        print("Try again. Error due to : {0}".format(ValError))
    finally:
        print("Executing finally clause\n")   '''    

new = 'README.md'
content = []
with open(new) as file_object:
    contents = file_object.read()
    

print(len(contents))

