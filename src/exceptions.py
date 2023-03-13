import sys


try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: invalid input.")
    sys.exit(1)
    
try:
    print(x / y)
except ZeroDivisionError:
    print("Error: can not divide by 0.")
    sys.exit(1)
