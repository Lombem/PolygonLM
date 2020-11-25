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

#Print a table of entered data and calculated values
print()
print(f"{'Point':>5} {'x':>10} {'y':>10}")
print("-" *43)
for i in range(polypts):
    print(f"{i+1:<5} {xcoords[i]:>10.2f} {ycoords[i]:>10.2f}") 

#Calculate the polygon geometry
Ax = 0
for i in range(polypts - 1):
    Ax = Ax + (xcoords[i+1] + xcoords[i]) * (ycoords[i+1] - ycoords[i]) #Area
print(f"{'Ax:':<5} {0.5*Ax:<10.2f}")


    
