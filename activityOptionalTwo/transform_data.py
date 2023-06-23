import pandas as pd
from pandas.core.frame import DataFrame
from datetime import datetime

columnsName = ['Producto', 'Referencia', 'Medida', 'Valor und']


def orderData(data: DataFrame):
    data_new = pd.DataFrame(columns=columnsName)
    # se filtran las columnas por nombre que inicie en  Referencia
    colsFilter = list(filter(lambda x: str(
        x).startswith('Referencia'), data.columns))

    # se inicia el proceso de organizar la data por colunas
    # 'Producto', 'Referencia', 'Medida', 'Valor und'
    for colName in colsFilter:
        # print(colName)
        findCols = []
        # se obtiene el index de la columna de la referencia
        indexCol = data.columns.get_loc(colName)
        # se agregan a la lsita de columnas por filtrar en el dataframe
        findCols.append('Producto')
        findCols.append(colName)
        # se ontiene  los nombres de la columnas siguientes de la colum referencia n°
        # y se agregan a la lsita de columnas por filtrar en el dataframe
        findCols.append(data.columns[(indexCol+1)])
        findCols.append(data.columns[(indexCol+2)])

        parcial_dat_frame = pd.DataFrame(data[findCols])
        parcial_dat_frame.columns = columnsName
        # print('*******************************')
        # print(parcial_dat_frame)
        # print('*******************************')
        data_new = pd.concat([data_new, parcial_dat_frame],
                             ignore_index=True)

    return data_new


def orderByColum(data: DataFrame, column):
    data = data.sort_values(by=[column])
    return data.reset_index(drop=True)


def getPriveByQuantity(lstReferencias: list, dataPrices: dict, dataSales: DataFrame):
    result = pd.DataFrame(columns=['Cantidad', 'fecha',
                          'Referencia', 'Valor_und', 'Total'])
    # print(dataSales)
    # print(lstReferencias)
    for ref in lstReferencias:
        valorUnd = dataPrices[ref]
        newData = dataSales[[ref, 'fecha']]
        newData.columns = 'Cantidad', 'fecha'
        newData['Referencia'] = ref
        newData['Valor_und'] = int(valorUnd)
        newData['Cantidad'].astype(int)
        newData['Total'] = newData.Cantidad*newData.Valor_und
        #newData['Mes'] = getMonth(newData.fecha)

       # print('newData ********************************')
        print(newData)
        result = pd.concat([result, newData],
                           ignore_index=True)

    print(result)
    return result


def getOnlyRef(dataPrices: DataFrame):
    lstRef = dataPrices['Referencia'].values.tolist()

    return lstRef


def getValuesPricesByReferencia(dataPrices: DataFrame):
    res = dict()
    columns = ['Referencia', 'Valor und']
    lstPrices = dataPrices[columns].to_dict('records')

    for v in lstPrices:
        res[v['Referencia']] = v['Valor und']

    return res


def getMonth(dateStr):
    month= ["January","February","March","April","May","June","July",
            "August","September","October","November","December"];
    insx=str(dateStr).split(sep='/')
    print(int(insx[1].replace('0',''))+1)
    return month[int(insx[1].replace('0',''))+1];
