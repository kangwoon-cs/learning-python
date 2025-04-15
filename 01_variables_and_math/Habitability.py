# Program Name: Habitability.py


from math import sqrt

# List of stars and their known exoplanets
# The list has the form that each record (inner lis) has the following fields:
# 1. Star name
# 2. Star temperature (in K)
# 3. Star radius (in solar radii)
# 4. List of lists of exoplanets orbiting that star, each record (inner list)
#    having the following fields:
#    1. Planet name
#    2. Orbital Distance (AU)

star_systems = [
    ["Sun", 5778, 1.0, [["Mercury", 0.39],
                        ["Venus", 0.72],
                        ["Earth", 1.0],
                        ["Mars", 1.52],
                        ["Jupiter", 5.20],
                        ["Saturn", 9.58],
                        ["Uranus", 19.22],
                        ["Neptune", 30.05]]],
    ["Proxima Centauri", 2992, 0.1542, [["Proxima Centauri b", 0.0485],
                                       ["Proxima Centauri d", 0.0289]]],
    ["Kepler-452", 5757, 1.11, [["Kepler-452b", 1.046]]],
    ["Kepler-62", 5062, 0.66, [["Kepler-62b", 0.0553],
                               ["Kepler-62c", 0.093],
                               ["Kepler-62d", 0.120],
                               ["Kepler-62e", 0.427],
                               ["Kepler-62f", 0.718]]],
    ["HD 209458", 6071, 1.20, [["HD 209458b", 0.047]]],
    ["LHS 1140", 3096, 0.216, [["LHS 1140c", 0.0270],
                                   ["LHS 1140b", 0.0946]]],
    ["Gliese 1214", 3111, 0.204, [["Gliese 1214b", 0.0149]]],
    ["55 Cancri A", 5172, 0.943, [["55 Cancri A e", 0.01544],
                                  ["55 Cancri A b", 0.1134],
                                  ["55 Cancri A c", 0.2373],
                                  ["55 Cancri A f", 0.7708],
                                  ["55 Cancri A d", 5.957]]],
    ["TRAPPIST-1", 2566, 0.1192, [["TRAPPIST-1b", 0.0115],
                                  ["TRAPPIST-1c", 0.0158],
                                  ["TRAPPIST-1d", 0.022],
                                  ["TRAPPIST-1e", 0.029],
                                  ["TRAPPIST-1f", 0.038],
                                  ["TRAPPIST-1g", 0.047],
                                  ["TRAPPIST-1h", 0.062]]]
]

# Constants
AUPerSolarRadii = 0.00465  # Number of AU per solar radius
absoluteZero = -273.15     # Absolute zero in Celsius
frozenTemp = 0             # Freezing point of water in Celsius
highestComplexTemp = 50    # Highest temperature for complex life in Celsius
boilingTemp = 100          # Boiling point of water in Celsius

# Declare two variables and one list to use accumulator pattern
cnt_planet = 0
cnt_habitable_planet = 0
habitability_data = []
# Using nested iteration to access all elements inside nested list
for stars in star_systems:
    star_name = stars[0]
    star_temp = stars[1]
    star_radi = stars[2]
    star_planets = stars[3]
    # print(f"{star_name:>17}  {star_temp:^5}K  {star_radi:.3f} solar radii")
    star_radi = star_radi * AUPerSolarRadii
    # print(f"{star_name:>17}  {star_temp:^5}K  {star_radi:.4f} AU")
    # radius of TRAPPIST-1: 0.0006 AU
    for planets in star_planets:
        planet_name = planets[0]
        planet_dist = planets[1]
        # print(f"{planet_name:>18}   {planet_dist} AU")
        # Calculate planets' surface temperature by given value
        planet_temp = star_temp*sqrt(star_radi/(2*planet_dist)) + absoluteZero
        # print(f"{planet_name:>18}: {planet_temp:>4.0f}C")
        # Make a classification of each star, if the star is habitable, +1 cnt_habitable_planet (accumulator pattern)
        if planet_temp < frozenTemp or planet_temp >= boilingTemp:
            classification = "uninhabitable"
        elif planet_temp > highestComplexTemp and planet_temp < boilingTemp:
            classification = "habitable only by simple life"
        elif planet_temp >= frozenTemp and planet_temp <= highestComplexTemp:
            classification = "habitable zone"
            cnt_habitable_planet += 1
        # +1 cnt_planet to know how many planets do we have     
        cnt_planet += 1
        # Add the value in form of list inside habitability_data
        habitability_data.append([planet_name,planet_temp,classification])

# Use iteration to print out all elements inside habitability_data
for data_planet in habitability_data:
    dt_plnt_name = data_planet[0]
    dt_plnt_temp = data_planet[1]
    dt_plnt_class = data_planet[2]
    print(f"{dt_plnt_name:>18}  ({dt_plnt_temp:>4.0f}C) is classified as {dt_plnt_class}.")

# Print the total number of planet and habitable planet 
print(f"- Of {cnt_planet} planets exmained found {cnt_habitable_planet} in the habitable zone.")

        

