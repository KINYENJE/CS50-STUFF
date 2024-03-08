import sys

try:   
  x= int(input("x: "))
  y= int(input("y: "))
except ValueError: # if the user inputs a string instead of a number then the program will exit with an error message 
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = int(x/y)
except ZeroDivisionError: # if the user inputs 0 as the value of y then the program will exit with an error message
    print("Error: Cannot divide by 0")
    sys.exit(1)

print(f"{x} / {y} = {result}")

