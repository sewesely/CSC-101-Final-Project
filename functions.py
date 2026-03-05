import data_processing

data = data_processing.load_auto_trends("AutomotiveTrendsData1975-2024(Prelim).csv")


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


#AutoFilter() - Sebastian Wesley
#Purpose: Using a provided "field" & "filter", returns a list of AutoTrendEntry classes that match
#Input: (list, str, str)
#Output: list
#Ex.: An input of (list[data_processing.AutoTrendEntry], "model_year", "1975") would returna list of AutoTrendEntry
    #that are only of the 1975
#How I'd complete as a computer?
    # I would iterate through each element in the list
    # check if the element has the attributes "field" and is equal to "filter"
    # if true then append to a new list
    # return the new list
def AutoFilter(data:list, field:str, filter:str)->list[data_processing.AutoTrendEntry]:
    filtered_data = []
    for Auto in data:
        if getattr(Auto,field) == filter:
            filtered_data.append(Auto)
    return filtered_data


#GreaterThan() - Sebastian Wesley
#Purpose: Using a provided list, "field", and float, returns a list of AutoTrendEntry classes that match
#Input: (list, str, str)
#Output: list
#Ex.: An input of (list[data_processing.AutoTrendEntry], "model_year", "1975") would returna list of AutoTrendEntry
    #that are only of the 1975
#How I'd complete as a computer?
    # I would iterate through each element in the list
    # check if the element has the attributes "field" and is equal to "filter"
    # if true then append to a new list
    # return the new list
def AutoFilter(data:list, field:str, filter:str)->list[data_processing.AutoTrendEntry]:
    filtered_data = []
    for Auto in data:
        if getattr(Auto,field) == filter:
            filtered_data.append(Auto)
    return filtered_data