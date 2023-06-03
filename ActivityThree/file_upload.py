import pandas as pd
import xml.etree.ElementTree as ET



def extract_excel(url, haderCol, idRow):
    try:
        # start directory
        data = pd.read_excel(url, header=haderCol,
                             index_col=idRow)
        return data
    except Exception as e:
        print("Error extract_excel: " + str(e))


def extract_from_csv(file_to_process):
    try:
        df = pd.read_csv(file_to_process)
        return df
    except Exception as e:
        print("Error extract_from_csv: " + str(e))


def extract_from_json(file_to_process):
    try:
        df = pd.read_json(file_to_process, lines=True)
        return df
    except Exception as e:
        print("Error extract_from_json: " + str(e))
   


def extract_from_xml(file_to_process):
    try:
        dataframe = pd.DataFrame(
            columns=['car_model', 'year_of_manufacture', 'price', 'fuel'])

        tree = ET.parse(file_to_process)
        root = tree.getroot()

        for person in root:
            car_model = person.find("car_model").text
            year_of_manufacture = int(person.find("year_of_manufacture").text)
            price = float(person.find("price").text)
            fuel = person.find("fuel").text
            dataframe = dataframe.append(
                {"car_model": car_model, "year_of_manufacture": year_of_manufacture, "price": price, "fuel": fuel}, ignore_index=True)

            return dataframe
    except Exception as e:
        print("Error extract_from_xml: " + str(e))
