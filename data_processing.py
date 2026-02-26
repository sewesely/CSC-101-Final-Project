from dataclasses import dataclass
from typing import Optional

#data_processing.py
    # converts the csv file of Auto Trends into a list of objects
    # where each object in said list represents 1 row in the csv

#Created with the help and guidance of:
    # https://realpython.com/python-csv/  <-- *like 90% of the info, very good website and quite extensive*
    # https://docs.python.org/3/library/dataclasses.html
    # https://realpython.com/python-data-classes/

#----------------------------------------------------------------------------------#
#This is the definition of the Dataclass
    # each element in "data" should be an object of this
    # use the class variables to find the data within the rows

@dataclass
class AutoTrendEntry:
    model_year: str           # "1975" all the way through "Prelim. 2024"
    regulatory_class: str     # "All", "Car", "Truck"
    vehicle_type: str         # "All", "Sedan/Wagon", "Pickup", etc.
    production_share: Optional[float]   # None if "-" (missing in some cells)
    mpg: Optional[float]                # None if "-" (missing in some cells)
    mpg_city: Optional[float]           # None if "-" (missing in some cells)
    mpg_hwy: Optional[float]            # None if "-" (missing in some cells)
    co2: Optional[float]                # None if "-" (missing in some cells)
    co2_city: Optional[float]           # None if "-" (missing in some cells)
    co2_hwy: Optional[float]            # None if "-" (missing in some cells)
    weight_lbs: Optional[float]         # None if "-" (missing in some cells)
    horsepower: Optional[float]         # None if "-" (missing in some cells)
    footprint_sqft: Optional[float]     # None if "-" (missing in some cells)


#Cleaning the csv for the function
    #some of the cells in the csv don't have data and are noted as "-"
    #this function helps the convert_auto_enty() ignore those cells
    #this function takes a str as an input which represent a singular cell
def parse_numeric(value: str) -> Optional[float]:
    """Returns None for '-' or empty strings, float otherwise."""
    val = value.strip()
    return None if val == "-" or val == "" else float(val) # removes str types from number only data

#converts the data of the row provided into 1 class
    #this function takes a dict as an input which represent a singular row
def convert_auto_entry(row: dict) -> AutoTrendEntry:
    return AutoTrendEntry(
        model_year       = row["Model Year"].strip(),
        regulatory_class = row["Regulatory Class"].strip(),
        vehicle_type     = row["Vehicle Type"].strip(),
        production_share = parse_numeric(row["Production Share"]),
        mpg              = parse_numeric(row["Real-World MPG"]),
        mpg_city         = parse_numeric(row["Real-World MPG_City"]),
        mpg_hwy          = parse_numeric(row["Real-World MPG_Hwy"]),
        co2              = parse_numeric(row["Real-World CO2 (g/mi)"]),
        co2_city         = parse_numeric(row["Real-World CO2_City (g/mi)"]),
        co2_hwy          = parse_numeric(row["Real-World CO2_Hwy (g/mi)"]),
        weight_lbs       = parse_numeric(row["Weight (lbs)"]),
        horsepower       = parse_numeric(row["Horsepower (HP)"]),
        footprint_sqft   = parse_numeric(row["Footprint (sq. ft.)"])
    )

import csv
#splits the csv into rows and passes each row to convert_auto_entry() and convert the row to a class
#return a list of objects, each object represents a row in the csv
def load_auto_trends(filepath: str) -> list[AutoTrendEntry]:
    entries = []
    with open(filepath) as f: #being honest not 100% sure what this line does
        reader = csv.DictReader(f)  # converts the csv into a list of dictionaries
        for row in reader:          # each row is a dict
            entries.append(convert_auto_entry(row)) # add the class of the row (function: dict -> class)
    return entries  # all the data, list[object]

data = load_auto_trends("AutomotiveTrendsData1975-2024(Prelim).csv")
