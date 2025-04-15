# Program Name: ExoFunctions.py
# Description: Modify an csv file named exoplanets (adding a temperature of each planet)

from pathlib import Path
from math import sqrt


def read_exoplanet_data(file_path :Path) -> list:
    """
    Find the file from path and returns a list of list which is consist of information of planets

    Parameters
    ----------
    file_path : Path
        The path of the csv file
    
    Returns
    exoplanet_data : list[list]
        The list of lists with each line in the csv file as an element    
    """

    # Run the following code if the file is found in the path
    if Path(file_path).is_file():
        # Create a empty list to use accumulator pattern
        exoplanet_data = []
        # Read the file and appends each elements inside the empty lists
        with open(file_path,"r") as exoplanet:
            lines = exoplanet.readlines()
            for line in lines:
                # Split strings into list
                plnt_list = line.strip().split(",")
                # Skipping the first line of csv file
                if plnt_list[1].isdigit():
                    exoplanet_data.append(plnt_list)
                else:
                    continue
        return exoplanet_data
    else:
        print(f"There's no file named in this path: {file_path}")


def deep_copy(data :list) -> list: 
    """
    Make a totally new copy of list (copy and save at the different memory location)

    Parameters
    ----------
    data : list
        Get a significant list from user and used to copy another list

    Returns
    -------
    copy : list
        Returns the copy of the original list but store in different memory location 
        so that not to change original list 
    """
    copy = []
    for sublist in data:
        copy.append(sublist.copy())
    return copy


def process_data(exo_data :list[list]) -> list:
    """
    Gets the list (data of planet's characteristics)
    and calculate the surface temperature of each planet
    returns a list of data with surface temperature appended

    Parameters
    ----------
    exo_data : list
        Original list of data (planet's characteristics)
    
    Returns
    -------
    copy_exo_data : list
        a deep copied new list of data (appended surface temperatures)
    """
     # Constants
    AUPerSolarRadii = 0.00465  # Number of AU per solar radius
        # Caculate the temperature of each planet
    copy_exo_data = deep_copy(exo_data)
    for planet in copy_exo_data:
        star_temp = float(planet[1])
        star_radi = float(planet[2])
        planet_dist = float(planet[4])
        star_radi = star_radi * AUPerSolarRadii
        planet_temp = star_temp*sqrt(star_radi/(2*planet_dist))
        # Add the planet's temperature to the list
        planet.append(int(planet_temp))
    return copy_exo_data


def print_data(prnt_list :list) -> None:
    """
    Gets the list as a parameter and print the list in an organized shape (planet's name and temperature)

    Parameters
    ----------
    prnt_list : list
        Original list of data
    
    Returns
    -------
    None
        It only prints out the list, not return any variables
    """
    print(f"{"Exoplanet_Name":<20} {"Temp":>7}")
    print("-"*29)
    for planet in prnt_list:
        name = planet[3]
        temp = planet[5]
        print(f"{name:<20}  {temp:5d}K")


def main():
   
    # Get the path of the csv file
    exoplanet_file = "exoplanets.csv"
    exoplanet_path = Path(exoplanet_file)

    exoplanet_data = read_exoplanet_data(exoplanet_path)
    final_data = process_data(exoplanet_data) # works great with this change
    # print(final_data)    
    # [['Sun', '5778', '1.0', 'Mercury', '0.39', 446], ['Sun', '5778', '1.0', 'Venus', '0.72', 328], 
    # ['Sun', '5778', '1.0', 'Earth', '1.0', 278], ['Sun', '5778', '1.0', 'Mars', '1.52', 225], 
    # ['Sun', '5778', '1.0', 'Jupiter', '5.2', 122], ['Sun', '5778', '1.0', 'Saturn', '9.58', 90], ... , 
    # ['TRAPPIST-1', '2566', '0.1192', 'TRAPPIST-1h', '0.062', 171]]

    # Print planet's name and temperature
    print_data(final_data) # works great with this change
    # Exoplanet_Name          Temp
    # -----------------------------
    # Mercury                 446K
    # Venus                   328K
    # ...
    # TRAPPIST-1g             197K
    # TRAPPIST-1h             171K


        # Write a new csv file
    output_file = Path("exoplanets_revised.csv")
    with open(output_file, "w") as outfile:
        outfile.write("StarName,StarTemp,StarRadius,ExoplanetName,ExoplanetDistance,ExoplanetTemp\n")
        for planets in exoplanet_data:
            data_dot_file = ""
            # Make a line of string (which includes all elements in a row)
            for data in planets:
                data_dot_file += str(data) + ","
            # Remove a comma at the end of string
            data_dot_file = data_dot_file[:-1]
            data_dot_file = data_dot_file + "\n"
            # Write a csv file adding each string
            outfile.write(data_dot_file)


if __name__ == "__main__":
    main()