#           DIPLOMADO MACHINE LEARNING
#
#               jose miguel lagos
#
#                actividad Opcional N°2
#
#  Corporación Unificada Nacional de Educación Superior
#
#              27 de Mayo de 2023
#


import glob
from extract_file import *
from transform_data import *
from shows_data import *

cant_refer = 3


def extractPrices():
    url = "data/PRODUCTOS.xlsx"
    excelData = extract_excel(url, 2)
    # print(excelData)

    return excelData


def loadSales():
    url = "data/ventas_papas.csv"
    dataCsv = extract_from_csv(url)

    return dataCsv


def main():
    print('Init process')
    dataPrices = extractPrices()
    dataPrices = orderData(dataPrices)
    dataPrices = orderByColum(dataPrices, 'Producto')
    dataSales = loadSales()
    pricesRef = getValuesPricesByReferencia(dataPrices)
    lstRef = getOnlyRef(dataPrices)
    dataRessult = getPriveByQuantity(lstRef, pricesRef, dataSales)
    #showcantSell(dataRessult)
    showcantSell2(dataRessult)
    # print(data)

    # print(data.columns[4])


main()
