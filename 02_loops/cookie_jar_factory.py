# Program Name: cookie_jar_factory

# Declare a jar, maximum, and limit before iteration starts
first_jar = 0
second_jar = 0
third_jar = 0
max_cookie = 45
cookie_limit = 20

while first_jar < max_cookie or second_jar < max_cookie or third_jar < max_cookie:
    # Get input from user (which jar do you want to fill)
    choosing_jar = input("Enter jar number (1, 2, or 3): ")
    jar_number = [1,2,3]
 
    # Check the input was vaild value
    if not choosing_jar.isdigit() or not int(choosing_jar) in jar_number:
        print("Please enter a valid jar number (1, 2, or 3).")
        continue
    # Typecasting the input value
    choosing_jar = int(choosing_jar) 

    # Get input from user (how many cookies you want to put in the jar)
    cookies_to_add = input("Enter cookies to add: ")
    # Check the input was valid value
    if not cookies_to_add.isdigit():
        print("Please enter a valid number.")
        continue
    # Typecasting the input value
    cookies_to_add = int(cookies_to_add)

    # If we add more than limit at once:
    if cookies_to_add > cookie_limit:
        print(f"Warning: You can't add more than {cookie_limit} cookies at once! Try again.")
        continue

    # Adding cookies into a jar
    if choosing_jar == 1:
        first_jar += cookies_to_add
        if first_jar > max_cookie:
            print(f"Oh no! The jar broke with {first_jar} cookies! ")
            first_jar -= cookies_to_add
            break
    
    elif choosing_jar == 2:
        second_jar += cookies_to_add
        if second_jar > max_cookie:
            print(f"Oh no! The jar broke with {second_jar} cookies! ")
            second_jar -= cookies_to_add
            break

    elif choosing_jar == 3:
        third_jar += cookies_to_add
        if third_jar > max_cookie:
            print(f"Oh no! The jar broke with {third_jar} cookies! ")
            third_jar -= cookies_to_add                     
            break 
    
    # Print the number of cookies
    print(f"Current number of cookies in Jar 1: {first_jar}, Jar 2: {second_jar}, Jar 3: {third_jar}")
    
# Print the final number of cookies
print(f"Final number of cookies in Jar 1: {first_jar}, Jar 2: {second_jar}, Jar 3: {third_jar} ")

# Print congratulation if all jar is full
if first_jar == max_cookie and second_jar == max_cookie and third_jar == max_cookie:
    print(f"All jars are perfectly full with {max_cookie} cookies each! Great job!")
