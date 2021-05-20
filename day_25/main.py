# with open("day_25/weather_data.csv") as data:
#     x = data.readlines()
#     print(x)

# import csv
# 
# with open("day_25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     temp = []
#     for i in data:
#         temperatures.append(i[1])
#     for i in range(1, len(temperatures)-1):
#         temp.append(int(temperatures[i]))
#     print(temp)
import pandas

# data = pandas.read_csv("day_25/weather_data.csv")
# print(data["temp"])
# temp_list = data["temp"].to_list()
# max_temp = max(temp_list)
# print(max_temp)
# print(data["condition"])
# print(data.condition)
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.temp*1.8 + 32) 

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# datas = pandas.DataFrame(data_dict)
# datas.to_csv("new_data.csv")

data = pandas.read_csv("day_25/central_park_squirel.csv")
gray = data["Primary Fur Color"][data["Primary Fur Color"] == "Gray"].count()
black = data["Primary Fur Color"][data["Primary Fur Color"] == "Black"].count()
cinnamon = data["Primary Fur Color"][data["Primary Fur Color"] == "Cinnamon"].count()
print(gray, black, cinnamon)

data_squirel = {
    "colors": ["gray", "black", "cinnamon"],
    "count": [gray, black, cinnamon]
}
data_s = pandas.DataFrame(data_squirel)
data_s.to_csv("squirel_color.csv")