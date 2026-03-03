import data_processing


#Purpose: Takes the data list and a year returns the average MPG is for that year.
#Input: list[AutoTrendEntry], str
#Output: float
#How would I do this as a computer?
#-Create a variable total_mpg and variable vehicle_counter and set both equal to 0
#-Iterate through the list using a for loop:
#   -If the entry is of the same year as the input:
#       -Add its mpg to mpg_total and add one to vehicle_counter
#-Divide mpg_total by vehicle_counter and return that
def avg_mpg_by_year(data:list[data_processing.AutoTrendEntry], year):
    total_mpg = 0
    vehicle_counter = 0
    for vehicle in data:
        if vehicle.model_year == year:
            total_mpg += vehicle.mpg
            vehicle_counter += 1
    return total_mpg/vehicle_counter