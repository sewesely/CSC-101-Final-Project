#Test
from data_processing import get_data
from functions import *

data = get_data()

#User Interface: - Sebastian Wesley
#Purpose: determines what data the user is interested in seeing
#Input: None (Inputs collected from user within the function)
#Output: None (Output is printed to the console)
#How I'd complete as a computer?
    # I would print a list of options that the user can choose from
    # Depending on what number the user chose, execute the function that corresponds to the number
    # Make sure the function loops in case the user gives an invalid input
def main_menu():
    print("Welcome to the Auto Trends Explorer!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Compare my car to others")
        print("2. See average CO2 emissions for a year")
        print("3. See highly efficient vehicles (mpg >= X)")
        print("4. See the stats of vehicles in a given year?")
        print("5. See how vehicles have improved over time?")
        print("6. Quit")

        choice = input("Enter a choice (1-6): ")

        if choice == "1":
            compare_user_car()
        elif choice == "2":
            show_avg_co2_for_year()
        elif choice == "3":
            show_high_efficiency_cars()
        elif choice == "4":
            show_vehicles_for_year()
        elif choice == "5":
            show_improvement()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


#compare_user_car() - Sebastian Wesley
#Purpose: Takes input from the user about their car and compares it to the data set
#Input: None (Inputs collected from user within the function)
#Output: None (Output is printed to the console)
#How I'd complete as a computer?
    # I would collect the user's vehicle data (year,type,mpg)
    # Then calculate the data of the user's vehicle type and of all vehicles
    # Use percent difference formula to give a clear answer of how the user's vehicle compares
    # Display all the data and add a comment on the data
def compare_user_car():
    print("\nCompare your vehicle to the others!")
    user_year = input("When was your car manufactured? (Valid from 1975-Prelim. 2024) ")
    print("Car Types: Sedan/Wagon, Pickup, Minivan/Van, Truck SUV, Car SUV")
    user_type = input("What type of car do you have? ")
    user_mpg = float(input("How efficient is your car? (MPG) "))

    avg_mpg_all = avg_mpg_by_year(data, user_year)
    avg_type_mpg = avg_mpg_by_year(AutoFilter(data, "vehicle_type", user_type), user_year)

    percent_difference = round((user_mpg - avg_type_mpg) / avg_type_mpg * 100, 1)

    print("\n#-------------------------------------------------------#")
    print("Your Car:\n Year: {}\n Type: {}\n MPG: {}\n".format(user_year, user_type, user_mpg))
    print("Average MPG for {} in {}: {}".format(user_type, user_year, round(avg_type_mpg,2)))
    print("Average MPG for all vehicles in {}: {}".format(user_year, round(avg_mpg_all,2)))

    if user_mpg >= avg_type_mpg:
        print("Your vehicle is {}% more efficient than the average {} in {}.".format(round(percent_difference,2), user_type, user_year))
        print("That's great for reducing fuel use and emissions over time!")
    else:
        print("Your vehicle is {}% less efficient than the average {} in {}.".format(abs(round(percent_diff,2)), user_type, user_year))
        print("Upgrading or driving less could significantly cut your fuel use and CO2 footprint.")
    print("#-------------------------------------------------------#")


#show_avg_co2_for_year() - Sebastian Wesley
#Purpose: For the provided year, prints the CO2 emissions and if the cars produced were efficient
#Input: None (Inputs collected from user within the function)
#Output: None (Output is printed to the console)
#How I'd complete as a computer?
    # Collect the wanted year from the user
    # pass the year onto avg co2 function
    # use the data from the function to determine if it was a decent year in terms of cars' emissions
def show_avg_co2_for_year():
    year = input("\nEnter a model year (1975-Prelim. 2024): ")
    avg_co2 = avg_co2_by_year(data, year)
    print("\n#-------------------------------------------------------#")
    print("Average real-world CO2 emissions in {}: {} g/mi".format(year,round(avg_co2,2)))

    if avg_co2 > 500:
        print("Vehicles in this year emit quite a lot of CO2 on average. Cleaner options can protect the environment.")
    elif avg_co2 > 400:
        print("Emissions are moderate, but there is still room for improvement in efficiency.")
    else:
        print("This year shows relatively low average emissions, reflecting more efficient or cleaner vehicles.")
    print("#-------------------------------------------------------#")



#show_high_efficiency_cars
#Purpose: using the user's provided minimum MPG, finds and prints the entries that meet that requirement
#Input: None (Inputs collected from user within the function)
#Output: None (Output is printed to the console)
#How I'd complete as a computer?
    # collect the minimum mpg from the user
    # use the greater/equal function to filter out all the Vehicle stats that don't meet the minimum requirements
    # Print the number of entries that pass
    # Print the entries that do pass (upto a limit since there can be upto 400 data entries...)
def show_high_efficiency_cars():
    try:
        threshold = float(input("\nShow vehicles with MPG greater or equal to: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    efficient_list = GreaterEqualThan(data, "mpg", threshold)
    if not efficient_list:
        print("No vehicles meet or exceed that MPG in the dataset.")
        return

    print("\n#-------------------------------------------------------#")
    print("Vehicles with MPG >= {}:".format(threshold))
    count = 0
    for entry in efficient_list:
        if count >= 15:
            break
        print("Year: {}, Type: {}, MPG: {}".format(entry.model_year,entry.vehicle_type,entry.mpg))
        count += 1

    print("\nTotal configurations meeting this threshold: {}".format(len(efficient_list)))
    print("Higher-MPG vehicles burn less fuel and emit less CO2 per mile, which is better for air quality and the climate.")
    print("#-------------------------------------------------------#")


#show_vehicles_for_year() - Sebastian Wesley
#Purpose: Using the year from the user, prints the vehicle's data of that year
#Input: None (Inputs collected from user within the fucntion)
#Output: None (Output is printed to the console)
#How I'd complete as a computer?
    # Collect the year to use the user
    # filter the data so you only have the entries of that year
    # Use the display function to nicely print filtered entries
def show_vehicles_for_year():
    year = input("\nEnter a model year (1975–Prelim. 2024): ")

    year_entries = AutoFilter(data, "model_year", year)

    if not year_entries:
        print("No data found for {}.".format(year))
        return

    print("\nVehicle configurations for {}:".format(year))
    display(year_entries)

#show_improvement() - Will Bakey
#Purpose: Takes two years and a field of interest and returns the percent change between the 2 years
#Input: None
#Output: None
#How would I do this as a computer?
#-Take an input for a past year, store it in a variable
#-Take another input for a more recent year, store in another variable
#-
def show_improvement():
    year1 = input("\nEnter a past year (1975-Prelim. 2024): ")
    year2 = input("\nEnter a more recent year (up to Prelim. 2024): ")
    field = input("\nWhat data are you interested in (Enter 'mpg' or 'co2'): ")
    percent_difference = round(percent_diff(year1, year2, field), 1)
    if field == "mpg":
        if percent_difference > 0:
            print("MPG improved by {}% from {} to {}!".format(percent_difference, year1, year2))
        else:
            print("MPG decreased by {}% from {} to {}".format(abs(percent_difference), year1, year2))
    elif field == "co2":
        if percent_difference < 0:
            print("CO2 emissions decreased by {}% from {} to {}!".format(abs(percent_difference), year1, year2))
        else:
            print("CO2 increased by {}% from {} to {}".format(percent_difference, year1, year2))



if __name__ == '__main__':
    main_menu()