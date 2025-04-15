# Program Name: ExoTemperatures.py
# Description: Modify an csv file named exoplanets (adding a temperature of each planet)


from pathlib import Path
from math import sqrt

# Constants
AUPerSolarRadii = 0.00465  # Number of AU per solar radius
# Get the path of the csv file
exoplanet_file = "exoplanets.csv"
exoplanet_path = Path(exoplanet_file)

# Run the following code if the file is found in the path
if Path(exoplanet_path).is_file():
    # Create a empty list to use accumulator pattern
    exoplanet_data = []
    # Read the file and appends each elements inside the empty lists
    with open(exoplanet_path,"r") as exoplanet:
        lines = exoplanet.readlines()
        for line in lines:
            # Split strings into list
            plnt_list = line.strip().split(",")
            # Skipping the first line of csv file
            if plnt_list[1].isdigit():
                exoplanet_data.append(plnt_list)
            else:
                continue
    
    # Caculate the temperature of each planet
    for planet in exoplanet_data:
        star_temp = float(planet[1])
        star_radi = float(planet[2])
        planet_dist = float(planet[4])
        star_radi = star_radi * AUPerSolarRadii
        planet_temp = star_temp*sqrt(star_radi/(2*planet_dist))
        # Add the planet's temperature to the list
        planet.append(int(planet_temp))
    
    # print(exoplanet_data)

    # Print planet's name and temperature
    print(f"{"Exoplanet_Name":<20} {"Temp":>7}")
    print("-"*29)
    for planet in exoplanet_data:
        name = planet[3]
        temp = planet[5]
        print(f"{name:<20}  {temp:5d}K")

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


else:
    print(f"There's no file named {exoplanet_file}")

