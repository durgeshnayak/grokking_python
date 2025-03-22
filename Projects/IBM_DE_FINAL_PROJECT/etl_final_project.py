import glob
import pandas as pd
from datetime import datetime

target_file = "./bank_market_cap_gbp.csv"


def extract_from_json(file_to_process):
    dataframe = pd.read_json(path_or_buf=file_to_process)

    return dataframe


def extract():
    extracted_data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])
    for json_file in glob.glob("./*.json"):
        extracted_data = extracted_data.append(extract_from_json(file_to_process=json_file), ignore_index=True)

    print(extracted_data.head(n=5))

    return extracted_data


def load_exchange_rates():
    exchange_rates_data = pd.read_csv(filepath_or_buffer="./exchange_rates.csv", index_col=0)
    exchange_rate_series = exchange_rates_data[exchange_rates_data.index == "GBP"]

    return float(exchange_rate_series["Rates"])


exchange_rate = load_exchange_rates()
print(exchange_rate)


def transform(ext_data):
    ext_data.rename(columns={'Market Cap (US$ Billion)': 'Market Cap (GBP Billion)'}, inplace=True)
    ext_data["Market Cap (GBP Billion)"] = round(ext_data["Market Cap (GBP Billion)"] * exchange_rate, 3)

    print(ext_data.head(n=5))

    return ext_data


def load(target, data_to_load):
    data_to_load.to_csv(target, index=False)


def log(message):
    timestamp_format = "%Y-%h-%d-%H:%M-%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(file="logfile.txt", mode="a") as file_stream:
        file_stream.write(timestamp + "," + message + "\n")


log("ETL JOB STARTED")

log("EXTRACT PHASE STARTED")
ext_data = extract()
log("EXTRACT PHASE COMPLETED")

log("TRANSFORM PHASE STARTED")
transformed_data = transform(ext_data)
log("TRANSFORM PHASE COMPLETED")

log("LOAD PHASE STARTED")
load(target_file, transformed_data)
log("LOAD PHASE COMPLETED")

log("ETL JOB COMPLETED")
