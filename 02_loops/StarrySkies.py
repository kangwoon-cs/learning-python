# Program Name: StarrySkies.py


print("Welcome to Starry Skies")

# Get the user input of rows and pattern multiplier
rows = int(input("Enter the number of rows of stars in cluster (in integer): "))
multi_pattern = int(input("Enter the pattern multiplier (in integer): "))

# Make a nested loop to print stars
# Using a range 1 to rows+1 because we don't need index 0 in this loop
for i in range(1, rows+1):
    # Calculate how many stars will show on screen
    num_stars = multi_pattern*(i*i)-(i%multi_pattern)
    # Printing stars repeatly number of num_stars 
    for n in range(num_stars):
        print("*",end='')
    # Printing number of stars at end of each row 
    print(f" ({num_stars})")    
        
