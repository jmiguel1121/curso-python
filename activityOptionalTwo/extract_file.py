import pandas as pd


def extract_excel(url, haderCol, idRow):
    try:
        # start directory
        data = pd.read_excel(url, header=haderCol,
                             index_col=idRow)
        return data
    except Exception as e:
        print("Error extract_excel: " + str(e))


def extract_excel(url, haderCol):
    try:
        # start directory
        data = pd.read_excel(url, header=haderCol)
        return data
    except Exception as e:
        print("Error extract_excel: " + str(e))


def extract_from_csv(file_to_process):
    try:
        df = pd.read_csv(file_to_process,delimiter=';')
        return df
    except Exception as e:
        print("Error extract_from_csv: " + str(e))
