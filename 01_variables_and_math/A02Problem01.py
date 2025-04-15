# Program Name: A02Problem01.py
# Description: This program will ask the user for the average distance of the
#   world from the Sun and return the orbital period.

# Get the average distance from the Sun from the user
# SyntaxError: '(' was never closed
# The parenthesis has not closed and it makes SyntaxError.
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'
# Also, it have the String value in variable a, we need to change it into float.
a = float(input("Enter average distance of world from Sun (in AU): "))

# Compute the orbital period of the world using Kepler's Third Law
# since P**2 = a**3 --> P = a**(3/2)
# I tested this for the Earth, that's enough, right?
# Semantic Error
# The original code: P = a**1 ouputs only correct answer when input is Earth's AU.
# I adjusted it so that the right output can come out at other values. 
P = a**(3/2)

# Display the orbital period of the world to the user
# NameError: name 'period' is not defined
# The name of variable "period" is not defined on this code, so it makes Runtime Error.
# I also changed the output format to make it easier to compare with the actual value.
print(f"The orbital period of this world is {P:.3f} years.")