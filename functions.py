import data_processing

data = data_processing.get_data()

#display() - Will Bakey
#Purpose: Takes a list of data entries and displays them in an organized way
#Input: list[data_processing.AutoTrendEntry])
#Output: None
#How would I do this as a computer?
#-Loop through the data list and print the attributes neatly for each entry
def display(data:list[data_processing.AutoTrendEntry])->None:
    entries = 0
    for entry in data:
        print("Year:", entry.model_year)
        print("Type:", entry.vehicle_type)
        print("MPG:", entry.mpg)
        print("CO2:", entry.co2)
        print("----------------")
        entries += 1
    print(entries, "entries")

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

#avg_mpg_by_year - Will Bakey
#Purpose: Takes the data list and a year returns the average MPG is for that year.
#Input: list[AutoTrendEntry], str
#Output: float
#Ex: avg_mpg_by_year(data, "2023") would output the average mpg of all cars in the year 2023
#How would I do this as a computer?
#-Create a variable total_mpg and variable vehicle_counter and set both equal to 0
#-Iterate through the list using a for loop:
#   -If the entry is of the same year as the input:
#       -Add its mpg to mpg_total and add one to vehicle_counter
#-Divide mpg_total by vehicle_counter and return that
def avg_mpg_by_year(data:list[data_processing.AutoTrendEntry], year:str)->float:
    total_mpg = 0
    vehicle_counter = 0
    filtered = AutoFilter(data, "model_year", year)
    for vehicle in filtered:
        total_mpg += vehicle.mpg
        vehicle_counter += 1
    return total_mpg/vehicle_counter

#avg_co2_by_year - Will Bakey
#Purpose: Takes the data list and a year as a string and returns the average co2 of all vehicles that year (g/mi)
#Input: list[AutoTrendEntry], str
#Output: float
#Ex: avg_co2_by_year(data, "2023") would output the average CO2 emissions (in g/mi) of all vehicle types in the year 2023
#How would I do this as a computer?
#-Create a total co2 emissions variable equal to 0
#-Create a vehicle counter variable equal to 0
#-Filter the data to be just of the specified year
#-Iterate through the filtered list and add each entry's co2 emissions to the
def avg_co2_by_year(data:list[data_processing.AutoTrendEntry], year:str)->float:
    total_co2 = 0
    vehicle_counter = 0
    filtered = AutoFilter(data, "model_year", year)
    for vehicle in filtered:
        total_co2 += vehicle.co2
        vehicle_counter += 1
    return total_co2/vehicle_counter

#GreaterEqualThan() - Sebastian Wesley
#Purpose: Using a provided list, "field", and float, returns a list of AutoTrendEntry classes are greater or equal to
    #the float
#Input: (list, str, float)
#Output: list
#Ex.: An input of (list[data_processing.AutoTrendEntry], "mpg", 10.0) would return a list of AutoTrendEntry
    #that have a mpg greater than 10
#How I'd complete as a computer?
    # I would iterate through each element in the list
    # check if the element has the attributes "field" and is greater or equal to the float
    # if true then append to a new list
    # return the new list
def GreaterEqualThan(data:list, field:str, min:str)->list[data_processing.AutoTrendEntry]:
    filtered_data = []
    for Auto in data:
        if getattr(Auto,field) >= min:
            filtered_data.append(Auto)
    return filtered_data

print(GreaterEqualThan(data, "mpg", 40.0))