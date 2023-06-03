from pandas.core.frame import DataFrame
from datetime import datetime
import pandas as pd
import glob

from file_upload import *
from transform import *

dir_out_files='out_files/'
order_by ='car_model'
tmpfile = "dealership_temp.tmp"               # store all extracted data
logfile = "dealership_logfile.txt"            # all event logs will be stored
targetfile = "dealership_transformed_data.csv"  # transformed data is stored


def extract():
    extracted_data = pd.DataFrame(
        columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])
    # for csv files
    for csvfile in glob.glob("dealership_data/*.csv"):
        print(csvfile)
        csvData = extract_from_csv(csvfile)
        extracted_data = pd.concat([extracted_data, csvData],ignore_index=True)

    # for json files
    for jsonfile in glob.glob("dealership_data/*.json"):
        jsonData = extract_from_json(jsonfile)
        extracted_data = pd.concat([extracted_data, jsonData],ignore_index=True)
    # for xml files
    for xmlfile in glob.glob("dealership_data/*.xml"):
        xmlData = extract_from_xml(xmlfile)
        extracted_data = pd.concat([extracted_data, xmlData],ignore_index=True)

    return extracted_data


def log(message):
    try:
        timestamp_format = '%H:%M:%S-%h-%d-%Y'
        # Hour-Minute-Second-MonthName-Day-Year
        now = datetime.now()  # get current timestamp
        timestamp = now.strftime(timestamp_format)
        with open("log/dealership_logfile.txt", "a") as f:
            f.write(timestamp + ',' + message + '\n')
    except Exception as e:
        print("Error log: " + str(e))


def main():
    createDir('log')
    log("ETL Job Started")
    log("Extract phase Started")
    extracted_data = extract()
    log("Extract phase Ended")
    log('Transform phase Started')
    transformed_data = transform(extracted_data)
    log("Transform phase Ended")
    log("Load phase Started")
    log("create directory out_files")
    createDir('out_files')
    log("Order data by cloum " + order_by)
    data_odered= orderByColum(transformed_data,order_by)
    log("load data to csv file")
    final_file =load(dir_out_files,targetfile, data_odered)
    log("Load phase Ended in "+final_file)
    log("ETL Job Ended")
    #print(data_odered)



main()
