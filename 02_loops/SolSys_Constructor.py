# Program Name: SolSys_Constructor.py


# Define a variable for greeting (I need this to use len() function)
Greeting = "Welcome to the Solar System Constructor"
print(Greeting)
# Print double underline right below greeting.
print("=" * len(Greeting))
print("You will be adding worlds to our Solar System.")

# Get a input from user on how much you want to add
repeat = int(input("How many worlds would you like to add? "))

# Declare a list to contain world's name and distances
# I chose the list format because the list is mutable, and to use the append function later in the code.
# I thought tuple and string data types were not fit in situations where content could be added and deleted inside.
world_names = []
world_dists = []

# Iteration  that repeats as many times as the number of variable "repeat"
for num in range(repeat):
    # Get the world-name input from user 
    name = input(f"Enter the name of world #{num}: ")
    # Add the input inside the "world_names" list
    world_names.append(name)
    # Get the world-distance input from user
    dists = float(input(f"Enter the distance of world #{num} from the Sun in AU: "))
    # Add the input inside the "world_dists" list
    world_dists.append(dists)

print(f"Let's compute the orbital periods for some of these worlds. \nChoose a range of worlds to analyze.")

# Get the index number input from user to determine where to start and where to end
index_start = int(input(f"Enter the starting index (0 to {len(world_names)}): "))
index_end = int(input(f"Enter the ending index (0 to {len(world_names)}): "))

# Repeatedly output using the data in the list as much as the range of the index number
for index in range(index_start,index_end+1):
    # Find the orbital period using kepler's law
    orb_period = world_dists[index] ** (3/2)
    # Outputs the element in the list that comes out using the index number and variable "orb_period"
    print(f"{world_names[index]} which is {world_dists[index]:.2f} AU from the Sun has a period of about {orb_period:.2f} Earth years.")