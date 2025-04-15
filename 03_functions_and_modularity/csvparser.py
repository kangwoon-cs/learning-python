# Name: Kangwoon Lee
# Description: Converts a CSV file into a nested dictionary using one of the columns as the key.

from pathlib import Path
import pprint

def csv2dod(filepath:Path, key_column:str='Name') -> dict:
    """
    Reads a CSV file and converts it into a dictionary of dictionaries.
    
    Parameters:
    filepath (Path): The path to the CSV file.
    key_column (str): The column name to be used as the key for the outer dictionary.

    Returns:
    csv_as_dict (dict): A dictionary where keys are values from the key_column, 
                        and values are dictionaries containing other column data.
    """

    # Create an empty dictionary to hold the CSV data.  This will be a
    # dictionary of dictionaries.  They key for the outer dictionary
    # will be the value in the key_column.
    csv_as_dict = {}

    # Check if the file exists, if it does, open it for reading.
    if filepath.exists() and filepath.is_file():
        with open(filepath, 'r') as file:
            # Read the first line of the file, which is the header.
            header = file.readline()

            # 2(a) TO DO: Strip the header of the newline character and
            # then split it into a list of column names called colNames

            colNames = header.strip().split(",")  ### FINISH BY UNCOMMENTING & DEFINING colNames
            # print(colNames) => ['Name,Role,Language,Salary,Location']
            # 2(b) TO DO: Rewrite the following empty dictionary
            # creation and loop as a one-line dictionary comprehension.
            # Also CLEARLY EXPLAIN IN A COMMENT what the dictionary
            # comprehension is doing.

            # Dictionary comprehension to map column names to their respective indexes.
            # This creates a dictionary where each key is a column name, and the value is its corresponding index in the CSV header.
            colNum = {colname: i for (i, colname) in enumerate(colNames)}
            # for i, colname in enumerate(colNames):
            #     colNum[colname] = i
            # print(colNum)
            # Read the rest of the file line by line
            for line in file:
                # 2(c)(1) TO DO: Strip the newline character from the
                # line and split it into a list of strings called `data`

                ### YOUR CODE HERE ###
                data = line.strip().split(",")
                


                # 2(c)(2) TO DO: We are going to build the inner
                # dictionary containing the rest of the data in this
                # line other than key_column value. We will eventually
                # assign this to csv_as_dict[key] where the key is the
                # key_column value.
                #
                # Get the value of the `key_column` column from this row
                # of `data` to use as the key for this dictionary entry.
                # You should get the column number (aka index) for the
                # key_column using your `colNum` dict!

                key = data[colNum[key_column]] ### UNCOMMENT & INSERT COLUMN NUMBER TO FINISH
                # print(key)
                # 2(c)(3) TO DO: Convert the following definition of an
                # empty inner_dict dictionary and loop that fills it
                # with data into a single dictionary comprehension. Also
                # clearly explain what the dictionary comprehension is
                # doing in a comment.

                # It maps each column name (except the key_column) to its corresponding value in the current row.
                # This creates a dictionary where the keys are column names and the values are the row's data.
                inner_dict = {colNames[i] : value for (i, value) in enumerate(data) if i != colNum[key_column]}
                # inner_dict = {}
                # for i, value in enumerate(data):
                #     if i != colNum[key_column]:
                #         inner_dict[colNames[i]] = value
                # print(inner_dict)
                # 2(d) TO DO: Assign the inner_dict dictionary to the
                # key key_column in the csv_as_dict dictionary.
                ### YOUR CODE HERE ###
                csv_as_dict[key] = inner_dict
                
                
    else:
        print(f"File {filepath} not found, empty dictionary returned.")

    return csv_as_dict


def main():
    """This function tests that the csv2dod function works correctly by
    loading a CSV file containing company roster data."""

    # 1(b) ADD COMMENTS HERE TO EXPLAIN THE PURPOSE OF THE FOLLOWING
    # CODE
    # get input (name of csv file) from the user and assigning dictionary of dictionaries to companyRoster
    input_csv = input("Enter the name of the CSV file: ")
    csv_path = Path(input_csv)
    companyRoster = csv2dod(csv_path, "Name")

    # 1(b) ADD COMMENTS HERE TO EXPLAIN THE PURPOSE OF THE FOLLOWING
    # CODE
    # Check the dictionary of dictionaries if it has created properly (checking the values of elements)
    if companyRoster:
        print("If your code works, the following should show matching values:")
        print(f" > {companyRoster['Aisha']['Role']} == 'Backend Developer'.")
        print(f" > {companyRoster['Fatima']['Language']} == 'Swift'.")
        print(f" > {companyRoster['Charles']['Location']} == 'Moorhead'.")
        print(f" > {companyRoster['Andre']['Salary']} == '54660'.")

    # The pprint module provides a capability to "pretty-print"
    # arbitrary Python data structures in a format that can be used as
    # input to the interpreter.  This is useful when you want to see the
    # structure of a complex data structure like a dictionary.
    print("\nHere's the entire dictionary:")
    pprint.pprint(companyRoster)


# Execute the main() function if this file is being run as a script.
if __name__ == "__main__":
    main()