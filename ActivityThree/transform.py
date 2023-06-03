import os
from pandas.core.frame import DataFrame
from datetime import datetime


def transform(data):
    data['price'] = round(data.price, 2)
    return data


def load(directory,targetfile, data_to_load):
    timestamp_format = '%H%M%S%h%d%Y'
        # Hour-Minute-Second-MonthName-Day-Year
    now = datetime.now()  # get current timestamp
    timestamp = now.strftime(timestamp_format)
    
    paht_name_file = directory + timestamp +'_'+targetfile
    data_to_load.to_csv(paht_name_file, sep=";", mode="a")
    
    return paht_name_file


def createDir(directory):
    print('it will create dir ' + directory)
    # valid if the directory exists
    if not os.path.isdir(directory):
        # If it doesn't exist, create it
        os.makedirs(directory)
        print('created dir' + directory)

def orderByColum(data:DataFrame,column):
    data = data.sort_values(by=[column])
    return data.reset_index(drop=True);