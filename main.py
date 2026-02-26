#Test
from data_processing import load_auto_trends, AutoTrendEntry

data = load_auto_trends("AutomotiveTrendsData1975-2024(Prelim).csv")

#testing data_processing.py
print(data)
print(len(data))
print(type(data),type(data[0]))
print(data[350])
x = 25
print("For {} in year {}, the average MPG on the HWY was {}"
      .format(data[x].vehicle_type, data[x].model_year, data[x].mpg_hwy))