import matplotlib.pyplot as plt
import numpy as np
from pandas.core.frame import DataFrame


def showcantSell(dataRessult: DataFrame):

    x = dataRessult[['fecha','Total']].groupby(['fecha'],as_index=False).mean()
    print(x)
    # mas colores
    # color y alpha. Alpha indica opacidad.
    x.plot(x='fecha', y='Total', kind="bar")
    plt.show()


def showcantSell2(dataRessult: DataFrame):
    x= dataRessult[['Referencia','Total','Cantidad']]
    print(x)
    ax = plt.gca()
    x.plot(kind='line',x='Referencia',y='Total',ax=ax)
    x.plot(kind='line',x='Referencia',y='Cantidad', color='red', ax=ax)
    plt.show()