# Name: Kangwoon Lee
# Description: Prints the average delay and the percentage of delayed flights for each airline.

from pathlib import Path
from csvparser import csv2dod
import pprint


def convert_values_to_float(this_dict):
    # Convert all the values stored in a dictionary to floats
    # using a dictionary comprehension
    this_dict = {key:float(value) for key,value in this_dict.items() }
    # for key, value in this_dict.items():
    #     this_dict[key] = float(value)
    return this_dict


def convert_inner_dict_values_to_float(this_dict):
    # Convert all the values stored in a dictionary to floats
    # using a dictionary comprehension
    new_dict = {key: convert_values_to_float(inner_dict) for key, inner_dict in this_dict.items()}
    return new_dict


def col2list(colName, flightsData):
    # FILL THIS IN!
    column = [inner_dict[colName] for inner_dict in flightsData.values()
              if colName in inner_dict]
    # for inner_dict in flightsData.values():
    #     if colName in inner_dict:
    #         column.append(inner_dict[colName])

    return column


def main():
    # Load the flight data which was obtained from the Bureau of
    # Transportation Statistics website and contains the flight delay
    # information for Fargo Hector field for the November 2024. The
    # columns are:
    # carrier_name: Airline name
    # arr_flights: Number of arriving flights at Hector
    # arr_del15: Number of late flights (defined as more than 15 minutes
    #            late)
    # arr_cancelled: Number of arriving flights cancelled
    # arr_diverted: Number of arriving flights diverted to other airport
    # arr_delay: Total delay in minutes for late flights due to any cause
    # carrier_delay: Total delay in minutes due to carrier action
    # weather_delay: Total delay in minutes due to weather
    # nas_delay: Total delay in minutes due to National Aviation System
    # security_delay: Total delay in minutes due to Security
    # late_aircraft_delay: Total delay in minutes due to late aircraft
    #                      arrival
    # total_delay: Total delay in minutes for all flights regardless of
    #              cause

    # Define the filename and filepath
    datapath = Path("Airline_Delay_Cause.csv")

    # Create a dictionary called `flightData` to hold the flight data
    # using the `csv2dod` function. Confirm that works, then convert the
    # values in the inner dictionaries to floats using the
    # `convert_inner_dict_values_to_float` function.
    flightData = csv2dod(datapath,"carrier_name")
    # Test to see if the data was loaded correctly
    # pprint.pprint(flightData["Delta"])


    flightData = convert_inner_dict_values_to_float(flightData)
    # pprint.pprint(flightData["Delta"]) 
    


    # Create lists of needed data from the CSV columns in the
    # dictionary, test the `col2list` function to see if it works.
    # print(col2list('arr_flights', flightData))

    # Find the average number of minutes late the late flights were for
    # each airline, regardless of the cause. Add comments to explain how
    # you calculated the average and what columns you used.

    # Calculate the average delay in minutes for late flights for each airline:
    # Formula used: (arr_delay / arr_del15)
    # arr_delay: Total delay in minutes for all late flights.
    # arr_del15: Number of flights delayed by more than 15 minutes.
    # If the number of delayed flights (arr_del15) is zero, set average delay to 0 to avoid division errors.

    num_delay = col2list('arr_del15', flightData)
    time_delay = col2list('arr_delay', flightData)
    avg_delay = [(avg := (time/num)) if num != 0 else 0 for num, time in zip(num_delay, time_delay)]
    # print(avg_delay)
    
    # for num, time in zip(num_delay,time_delay):
    #     if num != 0:
    #         avg = (time/num)
    #         avg_delay.append(avg)
    #     else:
    #         avg = 0
    #         avg_delay.append(avg)


    # Find the percentage of late flights for each airline. Add comments
    # to explain how you calculated the percentage and what columns you
    # used.

    # Calculate the percentage of late flights for each airline:
    # Formula used: (arr_del15 / arr_flights) * 100
    # arr_del15: Number of flights delayed by more than 15 minutes.
    # arr_flights: Total number of arriving flights.
    # If the total flights (arr_flights) is zero, set percentage to 0 to avoid division errors.
    
    tot_flight = col2list('arr_flights', flightData)
    percent_delayed = [(percent := (delayed/total)*100) if total != 0 else 0 for delayed, total in zip(num_delay,tot_flight)]
    
    # for delayed, total in zip(num_delay,tot_flight):
    #     if total != 0:
    #         percent = (delayed/total) * 100
    #         percent_delayed.append(percent)
    #     else:
    #         percent = 0
    


    # Print the results
    print("For November 2024 at Fargo Hector Field:")
    print(f"{"Airline":<16} {"Avg_Mins_Late":15} {"Percent_Late":>10}")
    print("---------------------------------------------")
    airlines = list(flightData.keys())
    for airline, minute, percent in zip(airlines,avg_delay,percent_delayed):
        print(f"{airline:16} {minute:9.2f} {percent:14.2f}% ")


# Execute the main() function if this file is being run as a script.
if __name__ == "__main__":
    main()