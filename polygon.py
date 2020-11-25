############################################################################################
# BIM A+ 3-2 Assignment 3; By: Lombe Mutale; 29 Nov. 2020                                  # 
# This program calculates mathematical properties of a polygon shape. The user enters the  #
# number of sides and the x and y coordinates in a counter clockwise manner. Results are   # 
# displayed with two decimal places.                                                       # 
############################################################################################

#Call library
import math

#Request number of points
polypts = int(input("Enter the number of polygon points: "))
print("Your polygon has " + str(polypts) + " polygon points.")

#A list that stores all coordinates - empty to start with
xcoords = []
ycoords = []

#Request coordinates
print("Enter the coordinates...")
for i in range(polypts):
    x = float(input(f"x[{i+1}] "))
    xcoords.append(x)
    y = float(input(f"y[{i+1}] "))
    ycoords.append(y)
print(f'{xcoords} {ycoords}')
    
