import pandas

FUR_COLORS = {
    "Gray": "grey",
    "Cinnamon": "red",
    "Black": "black",
}

with open(file="./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv", mode="r") as data_stream:
    raw_data = pandas.read_csv(filepath_or_buffer=data_stream)

data_dictionary = {}
fur_color_list = []
squirrel_count_list = []
raw_fur_colors = FUR_COLORS.keys()

for fur_color in raw_fur_colors:
    squirrel_color = FUR_COLORS[fur_color]
    filtered_data = raw_data[raw_data["Primary Fur Color"] == fur_color]
    squirrel_count = filtered_data["Primary Fur Color"].count()
    fur_color_list.append(squirrel_color)
    squirrel_count_list.append(squirrel_count)

data_dictionary["Fur Color"] = fur_color_list
data_dictionary["Count"] = squirrel_count_list

squirrel_count_data = pandas.DataFrame(data=data_dictionary)
squirrel_count_data.to_csv(path_or_buf="./squirrel_count_data.csv")





