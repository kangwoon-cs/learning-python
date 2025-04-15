# Program Name: A02Problem01.py
# Description: This program will ask the user for mass in kilograms
#    and return the radius to make it as a blackhole.

# set constant g, c
g = 6.674 * 10**(-11)
c = 299792458

# Testing Done: constant g, c printed properly.
# print(g,c)
# 6.674e-11 299792458

# get an input from user Type float
mass = float(input("Enter the mass of the object (in kg): "))

# Testing Done: the input from user is properly applied variable "mass" and type is also set up properly.
# print(mass,type(mass))
# Enter the mass (in kilograms): 3.5
# 3.5 <class 'float'>

# compute equation return radius in meter
radius = (2*g*mass)/(c**2)

# change the notation from meter to kilometer
radius = radius/1000

# Testing Done: equations and calculations work properly.
# print(radius)
# g = 2         g = 3
# mass = 2      mass = 4
# c = 2         c = 2
# 0.002         0.006



# print the final value of radius
print(f"The Schwarzschild radius of a black hole with mass 1.0 kg is {radius:.3g} km.")

# Testing Done: equations and calculations work properly.
# Enter the mass of the object (in kg): 1
# The Schwarzschild radius of a black hole with mass 1.0 kg is 1.49e-30 km.
# Enter the mass of the object (in kg): 1.9885e30
# The Schwarzschild radius of a black hole with mass 1.0 kg is 2.95 km.
