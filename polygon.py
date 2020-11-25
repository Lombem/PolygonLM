############################################################################################
# BIM A+ 3-2 Assignment 3; By: Lombe Mutale; 29 Nov. 2020                                  # 
# This program calculates mathematical properties of a polygon shape. The user enters the  #
# number of coordinates and the x and y coordinates in a counter clockwise manner.         # 
# Results are displayed with two decimal places.                                           # 
############################################################################################

#Request number of points
n = int(input("Enter the number of polygon points: "))

#Lists that stores all coordinates - empty to start with
x = []
y = []

#Request coordinates
print("Enter the coordinates...")
for i in range(n):
    xi = float(input(f"x[{i+1}] "))
    x.append(xi)
    yi = float(input(f"y[{i+1}] "))
    y.append(yi)

#Print a table of entered data and calculated values
print()
print(f"{'Point':>5} {'x':>10} {'y':>10}")
print("-" *43)
for i in range(n):
    print(f"{i+1:<5} {x[i]:>10.2f} {y[i]:>10.2f}") 

#Define the polygon geometry variables
Ax = 0
Sx = 0
Sy = 0
Ix = 0
Iy = 0
Ixy = 0

#Calculate the polygon geometry
for i in range(n - 1):
    Ax = Ax + (x[i+1] + x[i]) * (y[i+1] - y[i]) #Area
    Sx = Sx + (x[i+1] - x[i]) * (y[i+1]**2 + y[i]*y[i+1]+ y[i]**2) #Moment of area x
    Sy = Sy + (y[i+1] - y[i]) * (x[i+1]**2 + x[i]*y[i+1]+ x[i]**2) #Moment of area y
    Ix = Ix + (x[i+1] - x[i]) * (y[i+1]**3 + y[i]**2*y[i+1] + y[i+1]**2*y[i]+ y[i]**3) #Moment of inertia x
    Iy = Iy + (y[i+1] - y[i]) * (x[i+1]**3 + x[i]**2*y[i+1]+ x[i]*y[i+1]**2 + x[i]**3) #Moment of inertia y
    Ixy = Ixy + (y[i+1] - y[i]) * (y[i+1]*(3*x[i+1]**2 + 2*x[i]*x[i]+x[i]**2) + y[i]*(3*x[i]**2 + 2*x[i+1]*x[i] + x[i+1]**2))

#Finalise calculations    
Ax = 0.5*Ax
Sx = -Sx/6
Sy = Sy/6
Ix = -Ix/12
Iy = Iy/12
Ixy = -Ixy/24
xt = Sy/Ax
yt = Sx/Ax
Ixt = Ix - (yt**2*Ax)
Iyt = Iy - (xt**2*Ax)
Ixyt = Ixy + xt*yt*Ax

#Display the results 
print('Geometric characteristics: ') 
print(f"{'Ax:':<5} {Ax:<10.2f}")
print(f"{'Sx:':<5} {Sx:<10.2f}")
print(f"{'Sy:':<5} {Sy:<10.2f}")
print(f"{'Ix:':<5} {Ix:<10.2f}")
print(f"{'Iy:':<5} {Iy:<10.2f}")
print(f"{'Ixy:':<5} {Ixy:<10.2f}")
print(f"{'xt:':<5} {xt:<10.2f}")    
print(f"{'yt:':<5} {yt:<10.2f}")
print(f"{'Ixt:':<5} {Ixt:<10.2f}")
print(f"{'Iyt:':<5} {Iyt:<10.2f}")
print(f"{'Ixyt:':<5} {Ixyt:<10.2f}")        