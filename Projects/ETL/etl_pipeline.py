import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

tmpfile = "temp.tmp"
logfile = "logfile.txt"
target_file = "transformed_data.csv"


def extract_from_csv(file_to_process):
    df = pd.read_csv(filepath_or_buffer=file_to_process)
    return df


def extract_from_json(file_to_process):
    df = pd.read_json(path_or_buf=file_to_process, lines=True)
    return df


def extract_from_xml(file_to_process):
    df = pd.DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        df = df.append({"name": name, "height": height, "weight": weight}, ignore_index=True)
    return df


def extract():
    extracted_data = pd.DataFrame(columns=["name", "height", "weight"])

    # process all csv files
    for csv_file in glob.glob("./source/*.csv"):
        extracted_data = extracted_data.append(extract_from_csv(csv_file), ignore_index=True)

    # process all json files
    for json_file in glob.glob("./source/*.json"):
        extracted_data = extracted_data.append(extract_from_json(json_file), ignore_index=True)

    # process all xml files
    for xml_file in glob.glob("./source/*.xml"):
        extracted_data = extracted_data.append(extract_from_xml(xml_file), ignore_index=True)

    return extracted_data


def transform(data):
    data["height"] = round(data["height"] * 0.0254, 2)
    data["weight"] = round(data["weight"] * 0.45359237, 2)
    return data


def load(target, data_to_load):
    data_to_load.to_csv(target)


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
