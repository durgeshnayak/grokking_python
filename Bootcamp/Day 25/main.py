import pandas

with open(file="./weather_data.csv", mode="r") as data_stream:
    data = pandas.read_csv(filepath_or_buffer=data_stream)

    mean_temperature = round(data.temp.mean(), 2)
    print(f"The average temperature was: {mean_temperature}")

    max_temperature = data.temp.max()
    print(f"The maximum temperature was: {max_temperature}")
    day_with_max_temperature = data[data.temp == max_temperature]
    print(day_with_max_temperature)

    min_temperature = data.temp.min()
    print(f"The minimum temperature was: {min_temperature}")
    day_with_min_temperature = data[data.temp == min_temperature]
    print(day_with_min_temperature)

