# Program Name: ListyMcList.py

# Here's list of lists
lol = [ [1, 3, 6], [2, 4, 6, 7, 3], [2, 1],
       [5, 10, 3, 7, 2, 5, 9, 1], [ 3, 2, 1] ]
# Print list of lists
print(f"List of Lists : {lol}")

# Using enumerate() to get both index and each list in for loop
for i, listy in enumerate(lol):
    # Declare sum_num to saving sum of each list
    sum_num = 0
    for num in listy:
        # Adding each number of list in sum_num
        sum_num += num
    # Print each list and their sum
    print(f"Sum of {lol[i]} is {sum_num}")
