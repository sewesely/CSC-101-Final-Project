#Test
from data_processing import load_auto_trends, AutoTrendEntry, get_data
from functions import *

data = get_data()

#User Interface:
#Purpose: Takes input from the user about their car and compares it to the data set
#Input: None (Takes the user's input within the program)
#Output: None
def user_input():
    print("Hey want to compare your vehicle to the others?")
    while True:
        user_year = input("When was your car manufactored? (Valid from 1975-Prelim 2024) ")
        print("Car Types: Sedan/Wagon, Pickup, Minivan/Van, Truck SUV, Car SUV")
        user_type = input("What type of car do you have? ")
        user_mpg = float(input("How efficient is your car? (MPG) "))

        avg_mpg = avg_mpg_by_year(data, user_year)
        avg_type_mpg = avg_mpg_by_year(AutoFilter(data, "vehicle_type", user_type), user_year)

        percent_diff = round((user_mpg - avg_mpg)/avg_mpg*100, 3)

        print("Your Car:\n Year: {}\n Type: {}\n MPG: {}\n".format(user_year, user_type, user_mpg))
        print("Avg. MPG for {} in {}: {}\n".format(user_type, user_year, avg_type_mpg))

        if avg_type_mpg < user_mpg:
            print("Your vehicle is {}% more efficient than average for {}!".format(percent_diff, user_year))
        else:
            print("Your vehicle is {}% less efficient that average for {}".format(percent_diff, user_year))
            print("Maybe buy a newer car to be more efficient on the roads...")



if __name__ == '__main__':
    user_input()