# Heart Design With Python - Version 2

# Library
import math
from turtle import *

# The First Function Related To The First Calculations
def first(x):
    return 15 * math.sin(x) ** 3

# The Second Function Is Related To The Second Calculation
def second(x):
    return 12 * math.cos(x) - 5 * math.cos(2*x) - 2 * math.cos(3*x) - math.cos(4*x)


# Speed & Background Color
speed(2000)
bgcolor('black')

# Design
for i in range(360):
    x = first(math.radians(i)) * 10
    y = second(math.radians(i)) * 10
    goto(x, y)
    color('#F52375')
    goto(0, 0)
done()

# Finish
# Create By Moein Heshmati